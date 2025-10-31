# Kamel Potteries Bank Reconciliation App Architecture

## System Overview

```mermaid
graph TB
    A[User] --> B[Web Interface<br/>Streamlit]
    A --> C[Command Line<br/>Interface]
    B --> D[Data Processor]
    C --> D
    D --> E[Bank Statement<br/>Processor]
    D --> F[Xero Data<br/>Processor]
    E --> G[Reconciliation<br/>Engine]
    F --> G
    G --> H[Report<br/>Generator]
    H --> I[Output Files]
    H --> B
    J[Sample Data] --> D
    K[User Data] --> D
```

## Component Diagram

```mermaid
graph TB
    subgraph "Application Core"
        A[app.py<br/>Streamlit UI]
        B[cli.py<br/>Command Line]
        C[data_processor.py<br/>Data Processing]
        D[reconciliation_engine.py<br/>Matching Logic]
        E[report_generator.py<br/>Reporting]
        F[config.py<br/>Configuration]
        G[utils.py<br/>Utilities]
    end
    
    subgraph "Data Layer"
        H[data/sample_data<br/>Sample Files]
        I[data/uploads<br/>User Uploads]
        J[output<br/>Reports]
    end
    
    A --> C
    B --> C
    C --> D
    D --> E
    E --> J
    C --> F
    C --> G
    H --> C
    I --> C
```

## Data Flow

```mermaid
sequenceDiagram
    participant U as User
    participant W as Web Interface
    participant C as CLI
    participant P as Data Processor
    participant R as Reconciliation Engine
    participant G as Report Generator
    
    U->>W: Upload Files
    W->>P: Process Bank & Xero Data
    P->>R: Send Normalized Data
    R->>R: Match Transactions
    R->>G: Send Discrepancies
    G->>W: Return Reports
    W->>U: Display Results
    
    U->>C: Run CLI Command
    C->>P: Load Data Files
    P->>R: Send Normalized Data
    R->>R: Match Transactions
    R->>G: Send Discrepancies
    G->>C: Save Reports
    C->>U: Output File Paths
```

## File Processing Pipeline

```mermaid
graph LR
    A[Input Files] --> B[Data Processor]
    B --> C[Date Normalization]
    C --> D[Amount Conversion]
    D --> E[Data Validation]
    E --> F[Reconciliation Engine]
    F --> G[Date Matching]
    G --> H[Amount Matching]
    H --> I[Discrepancy Detection]
    I --> J[Report Generator]
    J --> K[Summary Reports]
    J --> L[Detailed CSV]
    J --> M[Action Plans]
```

## Technology Stack

- **Frontend**: Streamlit (Web Interface)
- **Backend**: Python 3.x
- **Data Processing**: Pandas, NumPy
- **File Handling**: Standard Python libraries
- **Reporting**: Custom report generation
- **Deployment**: Local installation

## Key Features

1. **Dual Interface**: Web UI and Command Line
2. **Flexible Data Processing**: Handles multiple CSV formats
3. **Configurable Matching**: Adjustable tolerance settings
4. **Comprehensive Reporting**: Multiple output formats
5. **Error Handling**: Robust error management
6. **Cross-Platform**: Works on Windows, macOS, and Linux

## Security Considerations

- All data processing happens locally
- No data is transmitted to external servers
- Files are processed in memory
- Temporary files are cleaned up automatically