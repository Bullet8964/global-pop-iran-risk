# Global Population & Geopolitical Risk Dashboard

## 📌 專案簡介
本專案為 AI 工具應用能力實作考之成果，結合 Python 自動化數據清理、Tailwind CSS RWD 前端繪製與 Chart.js 圖表化，呈現全球人口趨勢與伊朗地緣政治風險矩陣。

- **GitHub Pages 網址**：`https://<YOUR-USERNAME>.github.io/<YOUR-REPO-NAME>/`
- **一頁 PDF 報告**：請參閱本 Repo 根目錄下的 `report.pdf`

---

## 🤖 AI 使用聲明 (AI Usage Statement)
本專案開發過程中使用了 **ChatGPT / Claude** 輔助協助：
1. **程式碼生成**：協助撰寫 Python CAGR 計算邏輯與 HTML Tailwind RWD 排版。
2. **文本結構化**：協助歸納地緣政治風險因子，並嚴格區分「事實」與「推論」。

### 💡 Prompt 範例
> **Prompt:** "請寫一段 Python 腳本，讀取包含 2024, 2030, 2050, 2100 年人口數量的 raw.txt，計算平均值與整體 CAGR，並輸出為格式漂亮的 JSON 檔案。"

---

## 🔍 資料來源與驗證流程 (Data Verification)
### 1. 人口數據來源
本專案數據引用自 **UN World Population Prospects (2024 Revision)**。
- **AI 幻覺檢驗**：在對比 ChatGPT 與 Claude 提供的人口預測時，發現不同模型對於 2100 年的數字（10.3億 vs 10.4億）有些微偏差。
- **判斷與矯正**：最終以聯合國官方報告的中位數預測值（Medium Variant）為準（2100 年約 10.35 億），矯正 AI 的數據誤差。

### 2. 地緣政治風險（Iran Risk Matrix）
- **避免幻覺策略**：要求 AI 對每一個風險因子必須同時附上「可被驗證的事實數據 (Fact)」與「邏輯衍生推論 (Inference)」，不採納任何無具體機構（如 IAEA, EIA, World Bank）背書的猜測。

---

## 📁 檔案結構
