from flask import Flask, render_template_string, send_from_directory, request
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'results'
STATIC_FOLDER = 'static'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

DEFAULT_RESULT_FILE = "result_Apis_mellifera.zip"

filepath = os.path.join(RESULTS_FOLDER, DEFAULT_RESULT_FILE)
if not os.path.exists(filepath):
    with open(filepath, "w") as f:
        f.write(f"샘플 데이터 - {DEFAULT_RESULT_FILE}\n")


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(STATIC_FOLDER, filename)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(RESULTS_FOLDER, filename, as_attachment=True)

html_template = """<!DOCTYPE html>
<html lang='ko'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>DNA Analysis</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #eef2f3;
            margin: 0;
            padding: 0;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 30px;
            background: white;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        .header img {
            height: 60px;
        }
        .title-card {
            max-width: 1200px;
            margin: 20px auto 10px auto;
            padding: 15px;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            background: white;
            color: #1E3A8A;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .main-container {
            max-width: 1200px;
            margin: auto;
            padding: 10px;
            display: flex;
            justify-content: space-between;
            gap: 30px; /* 간격 일정하게 조정 */
        }
        .upload-container {
            width: 48%;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .upload-container h2 {
            text-align: center;
            color: #1E3A8A;
            margin-bottom: 20px;
        }
        .progress-results-container {
            width: 65%;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        .progress-box {
            background: black;
            color: limegreen;
            font-family: monospace;
            padding: 20px;
            border-radius: 6px;
            font-size: 16px;
            height: 220px;
            overflow-y: auto;
        }
        .progress-box h2, .results-box h2 {
            color: #1E3A8A;
        }
        .progress-box p {
            font-size: 18px;
            color: #444;
            font-weight: bold;
            margin-top: 15px;
        }
        .download-list {
            list-style: none;
            padding: 0;
            text-align: left;
        }
        .download-list li {
            background: #f8f9fa;
            padding: 10px;
            margin: 8px 0;
            border-radius: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .download-btn {
            background: #1E3A8A;
            color: white;
            border: none;
            padding: 6px 12px;
            cursor: pointer;
            border-radius: 6px;
            font-size: 14px;
        }
        .download-btn:hover {
            background: #162D65;
        }
        .file-group {
            display: flex;
            align-items: center;
            margin-top: 10px;
        }
        .file-group input {
            flex-grow: 1;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }
        .add-btn, .remove-btn {
            background: #1E3A8A;
            color: white;
            border: none;
            padding: 6px 12px;
            cursor: pointer;
            border-radius: 6px;
            font-size: 14px;
            margin-left: 8px;
        }
        .add-btn:hover {
            background: #162D65;
        }
        .remove-btn {
            background: #dc3545;
        }
        .remove-btn:hover {
            background: #c82333;
        }
        .submit-btn {
            display: block;
            width: 100%;
            background: #1E3A8A;
            color: white;
            border: none;
            padding: 12px;
            margin-top: 20px;
            cursor: pointer;
            border-radius: 6px;
            font-size: 16px;
            font-weight: bold;
        }
        .submit-btn:hover {
            background: #162D65;
        }
        @media (max-width: 768px) {
            .file-group {
                flex-direction: column;
                align-items: stretch;
            }
            .file-group input, .remove-btn {
                width: 100%;
            }
        }
    </style>
    <script>
        function addFileInput() {
            const fileList = document.getElementById('multiple-files');
            const div = document.createElement('div');
            div.className = 'file-group';

            const newInput = document.createElement('input');
            newInput.type = 'file';
            newInput.name = 'fa_files';
            newInput.accept = '.faa';

            const removeBtn = document.createElement('button');
            removeBtn.innerText = '- 삭제';
            removeBtn.className = 'remove-btn';
            removeBtn.onclick = function() {
                fileList.removeChild(div);
            };

            div.appendChild(newInput);
            div.appendChild(removeBtn);
            fileList.appendChild(div);
        }
    </script>
</head>
<body>
    <div class='header'>
        <img src='/static/기본형_심볼-03.jpg' alt='로고 좌측'>
        <img src='/static/logo(일반용).png' alt='로고 우측'>
    </div>

    <div class='title-card'>Generative Genes Searching Platform</div>

    <div class='main-container'>
        <div class='upload-container'>
            <h2>파일 업로드</h2>
            <form action='/upload' method='post' enctype='multipart/form-data'>
                <label>타겟 fasta 파일 업로드:</label>
                <div class="file-group">
                    <input type='file' name='single_fa' accept='.faa' required>
                </div>
                <br>
                
                <label>비교군 fasta 파일 업로드</label>
                <div id='multiple-files'></div>
                <button type='button' class='add-btn' onclick='addFileInput()'>+ 파일 추가</button>
                <br><br>
                <button type='submit' class='submit-btn'>🚀 제출</button>
            </form>
        </div>
        
        <div class='progress-results-container'>
            <div class='progress-box'>
                Apis processing start {{ timestamp }}<br>
                <br>
                Processing <span style="color: red;">OrthoFinder</span>...<br>
                Done<br>
                Processing <span style="color: orange;">BLASTp</span>...<br>
                Done<br>
                Processing <span style="color: yellow;">PyGAD</span>...<br>
                .
                .
                .
            </div>

            <div class='results-box'>
                <h2>결과 파일</h2>
                <ul class="download-list">
                    <li>
                        <span>result_Apis_mellifera.zip</span>
                        <a href="/download/result_Apis_mellifera.zip" class="download-btn">⬇ 다운로드</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</body>
</html>"""

@app.route('/')
def upload_form():
    result_files = os.listdir(RESULTS_FOLDER)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return render_template_string(html_template, timestamp=timestamp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
