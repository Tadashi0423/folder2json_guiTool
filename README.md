# Folder2JSON GUI Tool

## Introduction / 簡介

This is a simple GUI tool built with CustomTkinter that allows users to select a folder and convert its structure (including subfolders and files) into a JSON format. The tool provides a user-friendly interface to browse folders, generate the JSON, display it in a scrollable text area, and save it to a file.

這是一個使用 CustomTkinter 建置的簡單 GUI 工具，讓使用者選擇資料夾並將其結構（包括子資料夾和檔案）轉換成 JSON 格式。工具提供使用者友好的介面，用來瀏覽資料夾、生成 JSON、在可捲動文字區顯示，並保存到檔案。

![GUI Screenshot](https://github.com/Tadashi0423/folder2json_guiTool/blob/main/folder2json_guiTool_sample.png?raw=true)

## Features / 功能

- Browse and select a folder path.
- Generate a recursive JSON representation of the folder structure.
- Display the JSON in the GUI.
- Save the JSON to a file.
- Error handling for invalid paths.

- 瀏覽並選擇資料夾路徑。
- 生成資料夾結構的遞迴 JSON 表示。
- 在 GUI 中顯示 JSON。
- 將 JSON 保存到檔案。
- 對無效路徑的錯誤處理。

## Usage / 使用方式

### Recommended: Download from GitHub Releases / 推薦：從 GitHub Releases 下載

For most users, we recommend downloading the pre-built executable (.exe for Windows) from the [GitHub Releases](https://github.com/Tadashi0423/folder2json_guiTool/releases) page. This version is standalone and does not require Python or any dependencies to be installed. Simply download, run the .exe, and start using the tool.

對於大多數使用者，我們推薦從 [GitHub Releases](https://github.com/Tadashi0423/folder2json_guiTool/releases) 頁面下載預建的執行檔（Windows 的 .exe）。這個版本是獨立的，不需要安裝 Python 或任何依賴。只需下載、運行 .exe，即可開始使用工具。


### Running the Python Script / 運行 Python 腳本

If you want to run the source code (`folder2json_guiTool.py`) directly (e.g., for development or on other platforms), follow these steps:

如果您想直接運行原始碼（`folder2json_guiTool.py`）（例如用於開發或其他平台），請遵循以下步驟：

1. **Dependencies / 依賴條件**:
   - Python 3.6 or higher (tested on Python 3.12).
   - CustomTkinter: Install via `pip install customtkinter`.
   - Tkinter: Comes built-in with Python (no need to install separately).

   - Python 3.6 或更高版本（在 Python 3.12 上測試）。
   - CustomTkinter：透過 `pip install customtkinter` 安裝。
   - Tkinter：Python 內建（無需額外安裝）。

2. Clone the repository:
   ```
   git clone https://github.com/Tadashi0423/folder2json_guiTool.git
   cd folder2json_guiTool
   ```

   複製儲存庫：
   ```
   git clone https://github.com/Tadashi0423/folder2json_guiTool.git
   cd folder2json_guiTool
   ```

3. Install dependencies:
   ```
   pip install customtkinter
   ```

   安裝依賴：
   ```
   pip install customtkinter
   ```

4. Run the script:
   ```
   python folder2json_guiTool.py
   ```

   運行腳本：
   ```
   python folder2json_guiTool.py
   ```

## Building the Executable / 建置執行檔

If you want to build the .exe yourself, use PyInstaller:

如果您想自己建置 .exe，請使用 PyInstaller：

1. Install PyInstaller: `pip install pyinstaller`.
2. Run: `pyinstaller --onefile --windowed --add-data "path/to/customtkinter/assets/themes;customtkinter/assets/themes" folder2json_guiTool.py` (replace the part [path/to/customtkinter/assets/themes] to your path accordingly).

1. 安裝 PyInstaller：`pip install pyinstaller`。
2. 運行：`pyinstaller --onefile --windowed --add-data "path/to/customtkinter/assets/themes;customtkinter/assets/themes" folder2json_guiTool.py`（自行替換 [path/to/customtkinter/assets/themes] 為對應路徑）。

## License / 授權

This project is licensed under the MIT License.

此項目採用 MIT 授權。

---

