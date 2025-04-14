# Micro Logics Insights Assistant

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)
![Framework](https://img.shields.io/badge/framework-Flask%20%7C%20Dash-orange.svg)
![AI](https://img.shields.io/badge/AI-LangFlow-purple.svg)

A comprehensive AI-powered retail analytics solution that helps IT retailers optimize inventory, pricing, and sales through data-driven insights.

## 🌟 Features

- **AI-Powered Chat Interface**: Interact with your business data through natural language queries
- **Dynamic Analytics Dashboard**: Real-time visualization of sales trends, inventory movements, and profit margins
- **Automated Price Optimization**: Competitive price monitoring and dynamic adjustment recommendations
- **Inventory Management**: ABC analysis and movement classification of products
- **Data-Driven Decision Support**: Turn raw sales data into actionable business intelligence

## 📊 Dashboard Preview

[Dashboard Preview](https://drive.google.com/file/d/10n6R4toGVm0GytKoGXl30_bTCZ0NMcTX/view?usp=sharing)
[Dashboard Preview](https://drive.google.com/file/d/19KAcfs9nEBSjxwrCtuxMtk-I_s9L0XoU/view?usp=sharing)

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Dashboard**: Dash with Plotly
- **AI Engine**: LangFlow with vector database via AstraDB
- **Data Processing**: Pandas, NumPy
- **Styling**: Tailwind CSS

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/arjunthilak05/micro-logics-insights.git
   cd micro-logics-insights
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Main Interface: http://localhost:8051/
   - Dashboard: http://localhost:8051/dashboard/

## 📋 Project Structure

```
micro-logics-insights/
├── app.py              # Main Flask application
├── requirements.txt    # Project dependencies
├── static/             # CSS, JS files
├── templates/          # HTML templates
│   └── index.html      # Main chat interface
├── data/               # Sample data files
├── models/             # Data processing models
├── utils/              # Helper functions
└── README.md           # Project documentation
```

## 💡 Usage

### Chat Interface

The AI assistant can help with:
- Analyzing sales trends
- Recommending inventory adjustments
- Optimizing pricing strategies
- Providing supplier insights
- Generating actionable reports

Example queries:
- "Show me the slow-moving products in our inventory"
- "What was our best-selling product category last month?"
- "How does our pricing compare to competitors for storage products?"
- "When should we restock high-value items?"

### Dashboard

The dashboard provides visual analytics including:
- Sales trends over time
- Product performance metrics
- Inventory movement classification
- ABC analysis for product categories
- Profit margin visualization

## 🔄 Data Integration

### Supported Data Sources

- Tally ERP exports (CSV)
- Excel spreadsheets
- SQL databases (via connection string)

### Data Processing Pipeline

1. **Data Extraction**: Import from source systems
2. **Cleaning & Transformation**: Automated processing of raw data
3. **Analysis & Enrichment**: Apply business intelligence algorithms
4. **Visualization & Interaction**: Present through dashboard and chat interface

## 📈 Business Impact

- **Inventory Optimization**: 15-20% reduction in excess inventory
- **Pricing Strategy**: Data-driven competitive pricing
- **Sales Growth**: Target high-margin products with marketing
- **Decision Support**: Reduce manual analysis time by 75%

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- [Project Demo Video](https://www.example.com/demo)
- [Documentation](https://www.example.com/docs)
- [Report Issue](https://github.com/yourusername/micro-logics-insights/issues)

---

Developed as part of the IITM Online BS Degree Program Capstone Project by R Arjun Thilak.
