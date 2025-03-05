# 20250211 원준 수정

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
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Generative Genes Searching Platform</title>
  <!-- FontAwesome 아이콘 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" />
  <style>
    /* 공통 스타일 및 CSS 변수 */
    :root {
      --primary-color: #1A237E;
      --primary-hover: #283593;
      --bg-gradient-start: #E8EAF6;
      --bg-gradient-end: #F5F5F5;
      --text-color: #333;
      --card-bg: #ffffff;
      --shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      --transition-speed: 0.3s;
      --font-base: "Helvetica Neue", sans-serif;
      --base-font-size: 1rem;
    }
    body.dark {
      --bg-gradient-start: #121212;
      --bg-gradient-end: #1c1c1e;
      --card-bg: #1e1e1e;
      --text-color: #e0e0e0;
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: var(--font-base);
      font-size: var(--base-font-size);
      background: linear-gradient(135deg, var(--bg-gradient-start), var(--bg-gradient-end));
      color: var(--text-color);
      padding: 20px;
      transition: background var(--transition-speed), color var(--transition-speed);
      animation: fadeIn 0.8s ease-in-out;
      line-height: 1.6;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    main#main-content {
      max-height: calc(100vh - 160px);
      overflow-y: auto;
      padding-right: 10px;
    }
    header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--card-bg);
      padding: 1.25rem 2.5rem;
      box-shadow: var(--shadow);
      border-radius: 10px;
      margin-bottom: 0.625rem;
      position: relative;
    }
    .hamburger-btn {
      background: none;
      border: none;
      font-size: 1.75rem;
      cursor: pointer;
      color: var(--primary-color);
      transition: color var(--transition-speed);
      margin-right: 0.9375rem;
    }
    .hamburger-btn:hover,
    .hamburger-btn:focus {
      color: var(--primary-hover);
      outline: none;
    }
    .header-left {
      display: flex;
      align-items: center;
    }
    .header-left img {
      max-height: 3.125rem;
    }
    .header-title {
      flex-grow: 1;
      text-align: center;
      font-size: 3rem;
      font-weight: 700;
      background: linear-gradient(45deg, var(--primary-color), var(--primary-hover));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
    }
    .header-right {
      display: flex;
      align-items: center;
      gap: 1.25rem;
    }
    .toggle-dark-btn {
      background: none;
      border: none;
      font-size: 1.375rem;
      cursor: pointer;
      color: var(--primary-color);
      transition: color var(--transition-speed);
    }
    .toggle-dark-btn:hover,
    .toggle-dark-btn:focus {
      color: var(--primary-hover);
      outline: none;
    }
    /* 사이드바 (오프 캔버스 네비게이션) */
    #sidebar {
      position: fixed;
      top: 0;
      left: -250px;
      width: 250px;
      height: 100%;
      background: var(--card-bg);
      box-shadow: 2px 0 5px rgba(0,0,0,0.2);
      transition: left 0.3s ease;
      z-index: 200;
      padding: 1.25rem;
    }
    #sidebar.open {
      left: 0;
    }
    #sidebar .close-btn {
      background: none;
      border: none;
      font-size: 1.75rem;
      cursor: pointer;
      color: var(--primary-color);
      transition: color var(--transition-speed);
      margin-bottom: 1.25rem;
    }
    #sidebar .close-btn:hover,
    #sidebar .close-btn:focus {
      color: var(--primary-hover);
      outline: none;
    }
    #sidebar nav ul {
      list-style: none;
      padding: 0;
    }
    #sidebar nav ul li {
      margin-bottom: 0.9375rem;
    }
    #sidebar nav ul li a {
      text-decoration: none;
      color: var(--primary-color);
      font-size: 1.125rem;
      transition: color var(--transition-speed);
    }
    #sidebar nav ul li a:hover,
    #sidebar nav ul li a:focus {
      color: var(--primary-hover);
      outline: none;
    }
    .main-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 1.25rem;
    }
    /* 각 섹션 스타일 */
    section {
      background: var(--card-bg);
      padding: 1.875rem;
      border-radius: 12px;
      box-shadow: var(--shadow);
      min-height: 500px;
    }
    /* Hyperparameter Settings 영역은 원래 구현하신대로 */
    .hyperparam-container {
      min-height: 500px;
      max-height: 1080px;
      overflow-y: auto;
    }
    .project-settings {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.25rem;
      flex-wrap: wrap;
    }
    .project-name-input {
      flex-grow: 1;
      margin-right: 0.625rem;
      min-width: 200px;
    }
    .error-message {
      color: red;
      font-size: 1rem;
      margin-top: 0.25rem;
    }
    .success-message {
      color: green;
      font-size: 1rem;
      margin-top: 0.5rem;
    }
    input[type="text"],
    input[type="file"],
    select {
      width: 100%;
      padding: 0.625rem 0.9375rem;
      margin-bottom: 0.9375rem;
      border: 1px solid #ccc;
      border-radius: 8px;
      font-size: 1rem;
      transition: border var(--transition-speed);
      background: var(--card-bg);
      color: var(--text-color);
    }
    input[type="text"]:focus,
    select:focus {
      border-color: var(--primary-color);
      outline: none;
    }
    input[type="radio"] {
      margin-right: 0.5rem;
      transform: scale(1.2);
    }
    label {
      font-weight: 500;
      margin-bottom: 0.3125rem;
      display: block;
      color: var(--text-color);
    }
    .btn {
      background: var(--primary-color);
      color: #fff;
      border: none;
      font-size: 1.125rem;
      font-weight: 700;
      border-radius: 8px;
      padding: 0.75rem 1.875rem;
      transition: background var(--transition-speed);
      cursor: pointer;
      text-decoration: none;
      margin: 0.3125rem 0;
      display: inline-block;
    }
    .btn:hover,
    .btn:focus {
      background: var(--primary-hover);
      outline: none;
    }
    .submit-btn {
      width: 100%;
      margin-top: 1.25rem;
    }
    /* Step Control 영역 (원래 테두리 유지) */
    .step-control {
      display: flex;
      border: 2px solid var(--primary-color);
      border-radius: 8px;
      overflow: hidden;
      margin: 1.25rem 0;
    }
    .step-segment {
      flex: 1;
      text-align: center;
      padding: 0.875rem 0;
      cursor: pointer;
      background: transparent;
      transition: background var(--transition-speed), color var(--transition-speed);
      font-size: 1rem;
      color: var(--text-color);
    }
    .step-segment:hover,
    .step-segment:focus {
      background: rgba(26, 35, 126, 0.1);
      outline: none;
    }
    .step-segment.active {
      background: rgba(26, 35, 126, 0.2);
      color: var(--primary-color);
      font-weight: bold;
    }
    /* 다중 파일 입력란 및 삭제 버튼 - Comparison Fasta Files 영역 */
    #multiple-files {
      height: 300px;
      overflow-y: auto;
      padding-right: 5px;
      border: 1px solid #ccc;
      border-radius: 8px;
      margin-bottom: 0.9375rem;
    }
    .file-input-container {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.9375rem;
    }
    /* 삭제 버튼 스타일: 빨간색 배경, 흰색 '×' 아이콘, 적당한 크기의 정사각형 버튼 */
    .remove-btn {
      width: 32px;
      height: 32px;
      background-color: #ff4d4d;
      color: #fff;
      border: none;
      border-radius: 4px;
      font-size: 20px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      margin-left: 8px;
      padding: 0;
    }
    /* 터미널 박스 (기존 구현 그대로 유지) */
    .terminal-box {
      background: #1e1e1e;
      color: #0f0;
      padding: 1.25rem;
      border-radius: 8px;
      height: 600px;
      font-family: 'Consolas', monospace;
      font-size: 0.9375rem;
      overflow-y: auto;
      white-space: pre-wrap;
      margin-bottom: 0.9375rem;
    }
    .progress-section p {
      font-size: 1.125rem;
      margin: 1.25rem 0 0.625rem;
    }
    .results-area {
      background-color: rgba(26, 35, 126, 0.1);
      border: 2px solid var(--primary-color);
      border-radius: 8px;
      padding: 1.25rem;
      margin-top: 1.25rem;
      text-align: center;
      opacity: 0;
      transition: opacity 0.5s ease;
    }
    .results-area.visible {
      opacity: 1;
    }
    .results-area .results-message {
      font-size: 1.375rem;
      margin-bottom: 0.625rem;
      color: var(--primary-color);
    }
    .results-area .filename {
      font-size: 1.5rem;
      font-weight: bold;
      margin-bottom: 0.625rem;
    }
    .download-btn {
      font-size: 1.25rem;
      padding: 0.875rem 1.875rem;
    }
    .floating-btn {
      position: fixed;
      bottom: 80px;
      right: 20px;
      z-index: 100;
      border-radius: 50px;
      padding: 1.25rem 1.875rem;
      font-size: 1.25rem;
    }
    footer {
      background: var(--card-bg);
      padding: 1.25rem 2.5rem;
      border-top: 1px solid #ddd;
      font-size: 1rem;
      color: var(--text-color);
      margin-top: 2.5rem;
      text-align: center;
    }
    footer a {
      color: var(--primary-color);
      text-decoration: none;
    }
    footer a:hover,
    footer a:focus {
      text-decoration: underline;
      outline: none;
    }
    @media (max-width: 600px) {
      header {
        flex-direction: column;
        text-align: center;
      }
      .header-title {
        margin: 0.625rem 0;
        font-size: 2.5rem;
      }
      .header-right {
        margin-top: 0.625rem;
      }
      #sidebar {
        width: 200px;
        left: -200px;
      }
      #sidebar.open {
        left: 0;
      }
      .project-settings {
        flex-direction: column;
        align-items: stretch;
      }
      .project-name-input {
        margin-right: 0;
        margin-bottom: 0.625rem;
      }
      .floating-btn {
        bottom: 60px;
        right: 10px;
      }
      footer {
        padding: 1rem 1.25rem;
        font-size: 0.875rem;
      }
    }
  </style>
</head>
<body>
  <!-- 사이드바 (오프 캔버스 네비게이션) -->
  <div id="sidebar" aria-label="Navigation Menu">
    <button class="close-btn" onclick="toggleSidebar()" aria-label="Close Navigation Menu">
      <i class="fas fa-times"></i>
    </button>
    <nav>
      <ul>
        <li><a href="#home" tabindex="0">Home</a></li>
        <li><a href="#about" tabindex="0">About</a></li>
        <li><a href="#features" tabindex="0">Features</a></li>
        <li><a href="#contact" tabindex="0">Contact</a></li>
      </ul>
    </nav>
  </div>
  
  <!-- 헤더 영역 -->
  <header role="banner">
    <div class="header-left">
      <button class="hamburger-btn" onclick="toggleSidebar()" aria-label="Open Navigation Menu" aria-expanded="false">
        <i class="fas fa-bars"></i>
      </button>
      <img class="left-logo" src="https://physics.yonsei.ac.kr/uploads/media/eng_logo.png" alt="연세대학교 로고" />
    </div>
    <div class="header-title">Generative Genes Searching Platform</div>
    <div class="header-right">
      <button class="toggle-dark-btn" onclick="toggleDarkMode()" aria-label="Toggle Dark Mode">
        <i id="theme-icon" class="fas fa-moon"></i>
      </button>
    </div>
  </header>
  
  <!-- 메인 컨텐츠 영역 (내부 스크롤) -->
  <main id="main-content">
    <div class="main-container">
      
      <!-- 프로젝트 설정 및 파일 업로드 섹션 -->
      <section class="upload-container" aria-labelledby="upload-heading">
        <h2 id="upload-heading">Project Settings &amp; Input File</h2>
        <div class="project-settings" role="group" aria-labelledby="project-settings-label">
          <div class="project-name-input">
            <label id="project-settings-label" for="project-name">Project Name</label>
            <input type="text" id="project-name" name="project_name" required aria-describedby="project-error" />
            <span id="project-error" class="error-message" aria-live="polite"></span>
          </div>
          <button type="button" class="btn" onclick="saveProjectSettings()">Save</button>
        </div>
        <!-- 인라인 성공 메시지 -->
        <p id="project-save-message" class="success-message" aria-live="polite"></p>
        
        <h2>Input File</h2>
        <form id="upload-form" action="/upload" method="post" enctype="multipart/form-data">
          <h3>Target Fasta Files</h3>
          <input type="file" name="single_fa" accept=".fa,.fasta,.ffn,.frn,.fna,.faa" required />
          <h3>Comparison Fasta Files</h3>
          <div id="multiple-files">
            <!-- 초기 파일 입력란 (삭제 버튼 없이) -->
            <input type="file" name="comparison_fa[]" accept=".fa,.fasta,.ffn,.frn,.fna,.faa" required />
          </div>
          <button type="button" class="btn" onclick="addFileInput()">
            <i class="fas fa-plus"></i> Add More Files
          </button>
          
          <!-- Step Control 영역 -->
          <h2>Step Control</h2>
          <div class="step-control" role="group" aria-label="Step Control">
            <div class="step-segment" data-step="0" tabindex="0">OrthoFinder</div>
            <div class="step-segment" data-step="1" tabindex="0">BLASTp</div>
            <div class="step-segment" data-step="2" tabindex="0">PyGAD</div>
          </div>
          
          <!-- 업로드 진행 상황 프로그레스 바는 삭제되었습니다. -->
          
          <button type="submit" class="btn submit-btn">Upload</button>
        </form>
      </section>
      
      <!-- 하이퍼파라미터 설정 섹션 -->
      <section class="hyperparam-container" aria-labelledby="hyperparam-heading">
        <h2 id="hyperparam-heading">Hyperparameter Settings</h2>
        <!-- OrthoFinder Parameters -->
        <h3>OrthoFinder</h3>
        <label for="ortho_example1">Example parameter1</label>
        <select name="ortho_example1" id="ortho_example1">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
        <label for="ortho_example2">Example parameter2</label>
        <select name="ortho_example2" id="ortho_example2">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
        <label for="ortho_example3">Example parameter3</label>
        <select name="ortho_example3" id="ortho_example3">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
        <label for="ortho_example4">Example parameter4</label>
        <select name="ortho_example4" id="ortho_example4">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
        <label for="ortho_example5">Example parameter5</label>
        <select name="ortho_example5" id="ortho_example5">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
        <label for="ortho_value">E-Value</label>
        <input type="text" id="ortho_value" name="ortho_value" placeholder="e.g 0.01" />
        <span id="ortho-value-error" class="error-message" aria-live="polite"></span>
        
        <!-- BLASTp Parameters -->
        <h3>BLASTp</h3>
        <label for="blastp_example1">Example parameter1</label>
        <select name="blastp_example1" id="blastp_example1">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
        <label for="blastp_example2">Example parameter2</label>
        <select name="blastp_example2" id="blastp_example2">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
        <label for="blastp_example3">Example parameter3</label>
        <select name="blastp_example3" id="blastp_example3">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
        <label for="blastp_example4">Example parameter4</label>
        <select name="blastp_example4" id="blastp_example4">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
        <label for="blastp_example5">Example parameter5</label>
        <select name="blastp_example5" id="blastp_example5">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
        <label for="blastp_value">E-Value</label>
        <input type="text" id="blastp_value" name="blastp_value" placeholder="e.g 0.01" />
        <span id="blastp-value-error" class="error-message" aria-live="polite"></span>
        
        <!-- PyGAD Parameters -->
        <h3>PyGAD</h3>
        <label for="pygad_example1">Example parameter1</label>
        <select name="pygad_example1" id="pygad_example1">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
        <label for="pygad_example2">Example parameter2</label>
        <select name="pygad_example2" id="pygad_example2">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
        <label for="pygad_example3">Example parameter3</label>
        <select name="pygad_example3" id="pygad_example3">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
        <label for="pygad_example4">Example parameter4</label>
        <select name="pygad_example4" id="pygad_example4">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
        <label for="pygad_example5">Example parameter5</label>
        <select name="pygad_example5" id="pygad_example5">
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
          <option value="4">Option 4</option>
          <option value="5">Option 5</option>
        </select>
        <label for="pygad_value">E-Value</label>
        <input type="text" id="pygad_value" name="pygad_value" placeholder="e.g 0.01" />
        <span id="pygad-value-error" class="error-message" aria-live="polite"></span>
        
        <button type="button" class="btn" onclick="saveHyperparameters()">Save Hyperparameters</button>
        <!-- 인라인 성공 메시지 -->
        <p id="hyperparam-save-message" class="success-message" aria-live="polite"></p>
      </section>
      
      <!-- 진행 상태 섹션 (구현해놓은 그대로 유지) -->
      <section class="progress-section" aria-labelledby="progress-heading">
        <h2 id="progress-heading">Processing Status</h2>
        <div class="terminal-box" aria-live="polite">
          Processing Project Name Starts in ...
        </div>
        <h2>Save Results</h2>
        <div id="results-area" class="results-area hidden" aria-live="polite">
          <p class="results-message">
            <i class="fas fa-check-circle" style="color: green;" aria-hidden="true"></i>
            Your results are ready to download!
          </p>
          <p class="filename">Apis.zip</p>
          <button type="button" class="btn download-btn" aria-label="Download Results" title="Click here to download your results">💾 Download Results</button>
        </div>
      </section>
      
    </div>
  </main>
  
  <!-- Floating Run 버튼 -->
  <button class="btn floating-btn" aria-label="Run" title="Click here to run your project">▶ Run Project</button>
  
  <!-- 푸터 영역 -->
  <footer role="contentinfo">
    <p>Copyright © 2025 Yonsei University Smart Systems Lab. All Rights Reserved.</p>
  </footer>
  
  <script>
    // 사이드바 토글 및 접근성 강화 (ARIA 업데이트, 포커스 관리)
    function toggleSidebar() {
      const sidebar = document.getElementById("sidebar");
      const hamburgerBtn = document.querySelector(".hamburger-btn");
      const isOpen = sidebar.classList.toggle("open");
      hamburgerBtn.setAttribute("aria-expanded", isOpen);
      if (isOpen) {
        const firstLink = sidebar.querySelector("nav ul li a");
        firstLink.focus();
      } else {
        hamburgerBtn.focus();
      }
    }
    
    // ESC 키로 사이드바 닫기
    document.addEventListener("keydown", function(e) {
      if (e.key === "Escape") {
        const sidebar = document.getElementById("sidebar");
        if (sidebar.classList.contains("open")) {
          toggleSidebar();
        }
      }
    });
    
    // 바깥 영역 클릭 시 사이드바 닫기
    document.addEventListener("click", function(e) {
      const sidebar = document.getElementById("sidebar");
      const hamburgerBtn = document.querySelector(".hamburger-btn");
      if (sidebar.classList.contains("open") && !sidebar.contains(e.target) && !hamburgerBtn.contains(e.target)) {
        toggleSidebar();
      }
    });
    
    // 파일 입력 추가 및 삭제 기능 (삭제 버튼은 빨간색 x 표시가 된 정사각형 버튼)
    function addFileInput() {
      const container = document.getElementById("multiple-files");
      const fileInputContainer = document.createElement("div");
      fileInputContainer.classList.add("file-input-container");
      
      const newInput = document.createElement("input");
      newInput.type = "file";
      newInput.name = "comparison_fa[]";
      newInput.accept = ".fa,.fasta,.ffn,.frn,.fna,.faa";
      
      const removeBtn = document.createElement("button");
      removeBtn.type = "button";
      removeBtn.classList.add("remove-btn");
      removeBtn.textContent = "×"; // 빨간색 x 표시
      removeBtn.addEventListener("click", function() {
        container.removeChild(fileInputContainer);
      });
      
      fileInputContainer.appendChild(newInput);
      fileInputContainer.appendChild(removeBtn);
      container.appendChild(fileInputContainer);
    }
    
    // 다크 모드 토글 함수
    function toggleDarkMode() {
      document.body.classList.toggle("dark");
      const themeIcon = document.getElementById("theme-icon");
      if (document.body.classList.contains("dark")) {
        themeIcon.classList.remove("fa-moon");
        themeIcon.classList.add("fa-sun");
      } else {
        themeIcon.classList.remove("fa-sun");
        themeIcon.classList.add("fa-moon");
      }
    }
    
    // Step Control: 클릭 시 해당 인덱스까지 활성화
    const segments = document.querySelectorAll('.step-segment');
    segments.forEach((segment, index) => {
      segment.addEventListener('click', () => {
        segments.forEach((seg, i) => {
          if (i <= index) {
            seg.classList.add('active');
          } else {
            seg.classList.remove('active');
          }
        });
      });
      segment.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          segment.click();
        }
      });
    });
    
    // 프로젝트 이름 입력 필드 - 특수문자 필터링 및 빈 문자열 검사
    const projectNameInput = document.getElementById("project-name");
    const projectError = document.getElementById("project-error");
    projectNameInput.addEventListener("input", () => {
      let value = projectNameInput.value;
      const filteredValue = value.replace(/[<>&"'\/]/g, '');
      if (value !== filteredValue) {
        projectNameInput.value = filteredValue;
        projectError.textContent = "특수문자는 사용할 수 없습니다.";
      } else if (filteredValue.trim() === "") {
        projectError.textContent = "Project Name을 입력해 주세요.";
      } else {
        projectError.textContent = "";
      }
    });
    
    // 인라인 메시지로 프로젝트 설정 저장
    function saveProjectSettings() {
      if (projectNameInput.value.trim() === "") {
        projectError.textContent = "Project Name을 입력해 주세요.";
        return;
      }
      const msg = document.getElementById("project-save-message");
      msg.textContent = "Project Name saved.";
      setTimeout(() => { msg.textContent = ""; }, 3000);
    }
    
    // 인라인 경고를 포함한 하이퍼파라미터 저장 함수 (E-Value 값은 0과 1 사이의 숫자만 허용)
    function saveHyperparameters() {
      let valid = true;
      const eValueRegex = /^(0(\.\d+)?|1(\.0+)?)$/;
      
      const orthoValue = document.getElementById("ortho_value").value.trim();
      const blastpValue = document.getElementById("blastp_value").value.trim();
      const pygadValue = document.getElementById("pygad_value").value.trim();
      
      if(orthoValue === "") {
        document.getElementById("ortho-value-error").textContent = "E-Value를 입력해 주세요.";
        valid = false;
      } else if (!eValueRegex.test(orthoValue)) {
        document.getElementById("ortho-value-error").textContent = "0과 1 사이의 숫자만 입력하세요.";
        valid = false;
      } else {
        document.getElementById("ortho-value-error").textContent = "";
      }
      
      if(blastpValue === "") {
        document.getElementById("blastp-value-error").textContent = "E-Value를 입력해 주세요.";
        valid = false;
      } else if (!eValueRegex.test(blastpValue)) {
        document.getElementById("blastp-value-error").textContent = "0과 1 사이의 숫자만 입력하세요.";
        valid = false;
      } else {
        document.getElementById("blastp-value-error").textContent = "";
      }
      
      if(pygadValue === "") {
        document.getElementById("pygad-value-error").textContent = "E-Value를 입력해 주세요.";
        valid = false;
      } else if (!eValueRegex.test(pygadValue)) {
        document.getElementById("pygad-value-error").textContent = "0과 1 사이의 숫자만 입력하세요.";
        valid = false;
      } else {
        document.getElementById("pygad-value-error").textContent = "";
      }
      
      if (!valid) return;
      
      const msg = document.getElementById("hyperparam-save-message");
      msg.textContent = "Hyperparameters saved.";
      setTimeout(() => { msg.textContent = ""; }, 3000);
    }
  </script>
</body>
</html>
"""

@app.route('/')
def upload_form():
    result_files = os.listdir(RESULTS_FOLDER)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return render_template_string(html_template, timestamp=timestamp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
