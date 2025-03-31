# Design Document

By hongjiNH

## Scope

The purpose of this database:
1. To track freelance projects, clients and payment.
2. To keep track of on going and completed projects.
3. To monitor payment statuses
4. To manage client information in one place

The entities included in the scope of the database are:

_Clients_: Presents all clients. It includes attributes such as
    client_id,name,email,phone,company,notes

_Projects_: Presents all projects. It includes attributes such as
    project_id,client_id,title,description,start_date,deadline,status

_Invoices_:Presents all invoices. It includes attributes such as
    invoice_id,project_id,amount,due_date,paid_status


## Functional Requirements
1. Client Management
    - Add, updating client details
    - Each client must have a unique email address
    - Search for clients by name, email or company
2. Project Management
    - Create new projects for clients
    - Have status like Pending, In progress, Completed, On Hold
    - Update project details, including deadlines and descriptions
    - List all projects for a specific client
    - Delete project
3. Invoice Management
    - Generate invoices linked to projects
    - Track that whether the invocie has been paid or unpaid or overdue
    - Filter invoices by status and due date.

4. Tracking
    - Able to view total outstanding payment
    - Generate a list of overdue invoices
    - Generate completed project per client
## Representation

### Entities

The entities represented in the database are:

1. **clients**:
    - Attributes: client_id (auto-incremented), name, email, phone, company, notes
    - Types: cliend_id (INT), name (VARCHAR(255) NOT NULL) , email (VARCHAR(255) UNIQUE NOT NULL) , phone (VARCHAR(50)), company (VARCHAR(255)), notes (TEXT)
    - Constraints:
        1. client_id is PK
        2. name NOT NULL
        3. email must be UNIQUE and NOT NULL

2. **projects**
    - Attributes: project_id (auto-incremented), client_id, title, description, start_date, deadline, status
    - Types: project_id (INT), client_id (INT), title (VARCHAR(255) NOT NULL), description (TEXT), start_date (DATE NOT NULL), start_date (DATE NOT NULL), deadline (DATE NOT FULL), status (VARCHAR(50) CHECK (status IN ('Pending', 'In Progress', 'Completed', 'On Hold')))
    - Constraints:
        1. project_id is PK
        2. client_id is FK
        3. title is NOT NULL
        4. start_date is NOT NULL
        5. deadline is NOT NULL
        6. status must be one of the following('Pending', 'In Progress', 'Completed', 'On Hold')

3. **invoices**
    - Attributes: invoice_id (auto-incremented), project_id, amount, due_date, paid_status
    - Types: invoice_id (INT), project_id (INT NOT NULL), amount (DECIMAL(10,2) NOT NULL), due_date (DATE NOT NULL), paid_status ( VARCHAR(50) CHECK (paid_status IN ('Unpaid', 'Paid', 'Overdue')))
    - Constraints:
        1. invoice_id is PK
        2. project_id is FK
        3. amount is NOT NULL
        4. due_date is NOT NULL
        5. paid_status must be one of the following('Pending', 'In Progress', 'Completed', 'On Hold')

### Relationships

![alt text](https://github.com/hongjiNH/CS50/blob/main/SQL/project/sql.png?raw=true)

In this section you should include your entity relationship diagram and describe the relationships between the entities in your database.

1. Clients having multiple projects.
2. Projects generating multiple invoices.

## Optimizations

The following optimizations have been implemented:
- Indexes: Have been created on client name, invoices status to improve search performance.
