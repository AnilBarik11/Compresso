// ==UserScript==
// @name         Gemini Prompt Compressor & File Uploader
// @namespace    http://tampermonkey.net/
// @version      1.9
// @description  Combined Text Compressor and File Uploader with Append Support
// @author       Anil
// @match        https://gemini.google.com/*
// @grant        GM_xmlhttpRequest
// @connect      127.0.0.1
// ==/UserScript==

(function() {
    'use strict';

    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.style.display = 'none';
    document.body.appendChild(fileInput);

    function getElements() {
        return {
            container: document.querySelector('.input-area-container') || document.querySelector('div[contenteditable="true"]')?.parentElement,
            inputBox: document.querySelector('div[contenteditable="true"]')
        };
    }

    function injectUI() {
        const { container, inputBox } = getElements();
        if (!container || !inputBox || document.getElementById('compress-wrapper')) return;

        const wrapper = document.createElement('div');
        wrapper.id = 'compress-wrapper';
        wrapper.style.cssText = 'display: flex; gap: 8px; margin: 8px;';

        const btnCompress = document.createElement('button');
        btnCompress.innerText = '✨ Compress';
        btnCompress.style.cssText = 'background:#1a73e8; color:white; border:none; padding:8px 14px; border-radius:20px; cursor:pointer; font-size:12px;';

        btnCompress.onclick = () => {
            btnCompress.innerText = '...';
            btnCompress.disabled = true;
            GM_xmlhttpRequest({
                method: 'POST',
                url: 'http://127.0.0.1:8000/compress',
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify({ text: inputBox.innerText }),
                onload: (res) => {
                    btnCompress.innerText = '✨ Compress';
                    btnCompress.disabled = false;
                    try {
                        const data = JSON.parse(res.responseText);
                        inputBox.innerText = data.compressed_text;
                        inputBox.dispatchEvent(new Event('input', { bubbles: true }));
                    } catch (e) { alert("Parsing Error"); }
                },
                onerror: () => { btnCompress.innerText = '✨ Compress'; btnCompress.disabled = false; alert("Server Error"); }
            });
        };

        const btnUpload = document.createElement('button');
        btnUpload.innerText = '📁 Upload File';
        btnUpload.style.cssText = 'background:#34a853; color:white; border:none; padding:8px 14px; border-radius:20px; cursor:pointer; font-size:12px;';
        btnUpload.onclick = () => fileInput.click();

        wrapper.appendChild(btnCompress);
        wrapper.appendChild(btnUpload);
        container.appendChild(wrapper);
    }

    fileInput.onchange = (e) => {
        const file = e.target.files[0];
        if (!file) return;

        const btnUpload = document.getElementById('compress-wrapper')?.lastChild;
        if (!btnUpload) return;

        btnUpload.innerText = 'Uploading...';
        btnUpload.disabled = true;

        const formData = new FormData();
        formData.append('file', file);

        GM_xmlhttpRequest({
            method: 'POST',
            url: 'http://127.0.0.1:8000/compress-file',
            data: formData,
            onload: (res) => {
                btnUpload.innerText = '📁 Upload File';
                btnUpload.disabled = false;
                try {
                    const data = JSON.parse(res.responseText);
                    const { inputBox } = getElements();
                    if (inputBox && data.compressed_text) {
                        inputBox.innerText += "\n" + data.compressed_text;
                        inputBox.dispatchEvent(new Event('input', { bubbles: true }));
                    } else { alert("Server returned error: " + (data.detail || "Unknown")); }
                } catch (e) { alert("Parsing Error!"); }
            },
            onerror: () => {
                btnUpload.innerText = '📁 Upload File';
                btnUpload.disabled = false;
                alert("Upload failed! Ensure Python server is running.");
            }
        });
        fileInput.value = '';
    };

    setInterval(injectUI, 1000);
})();