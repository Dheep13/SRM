```mermaid
flowchart TD
    A["Start: (5,2)
    🔵🔵🔵🔵🔵|🔵🔵"] --> B["(5,0)
    🔵🔵🔵🔵🔵|  
    Empty small jug"]
    
    B --> C["(3,2)
    🔵🔵🔵|🔵🔵
    Pour big to small"]
    
    C --> D["(3,0)
    🔵🔵🔵|
    Empty small jug"]
    
    D --> E["(1,2)
    🔵|🔵🔵
    Pour big to small"]
    
    E --> F["Goal: (1,0)
    🔵|
    Empty small jug"]

    style A fill:#e6f3ff,stroke:#333
    style F fill:#d1ffd1,stroke:#333
    
    %% Add labels to show the action numbers
    A -- "Action 2" --> B
    B -- "Action 4" --> C
    C -- "Action 2" --> D
    D -- "Action 4" --> E
    E -- "Action 2" --> F