# ProcureIt

ProcureIt is a procurement management application designed to simplify and streamline the procurement process for organizations. It enables efficient management of purchase requests, approvals, and vendor interactions.

## Team

- Carlos Ageng`o – Software Architect and Full Stack Developer, UI/UX Designer

## Roles

- **Software Architect (Carlos Ageng`o):** Oversees the overall development process, handles project documentation, and leads backend and frontend development, ensuring an intuitive user experience.
  
- **User Interface and User Experience Design (Carlos Ageng`o):** Designs user interfaces for simplicity and visual appeal.

## Technologies

### Backend

- Python (Flask framework)
- MySQL database

### Frontend

- HTML
- CSS
- JavaScript

### Other Technologies

- Git for version control
- GitHub for collaboration and repository management

## Alternative Technology Choices

1. **Backend:** Django instead of Flask. Flask was chosen for its flexibility, aligning better with the project's simplicity and specific requirements.

2. **Database:** Contemplated using PostgreSQL as an alternative to MySQL. MySQL was chosen for its widespread adoption, robust performance, and compatibility with Python libraries.

## Challenge

### Problem Statement

The ProcureIt application aims to simplify and streamline the procurement process for organizations, allowing for efficient management of purchase requests, approvals, and vendor interactions.

### What the Project Will Not Solve

ProcureIt will not handle financial transactions or payment processing. It will focus solely on procurement management.

## Target Users

The application will cater to procurement teams within organizations of various sizes, helping them manage purchase requests, track approvals, and communicate with vendors effectively.

## Locale Dependency

ProcureIt is designed to be locale-independent, ensuring usability across different regions and languages.

## Risks

### Technical Risks

- **Database Scalability:** Implementing database optimization techniques and considering sharding if necessary to address scalability issues with the MySQL database.

- **Integration Complexity:** Thorough API compatibility tests and backup plans in case of any integration issues with third-party APIs.

### Non-Technical Risks

- **User Adoption:** Providing comprehensive training and support to ensure a smooth transition from existing procurement processes.

- **Regulatory Compliance:** Conducting regular compliance audits and staying up-to-date with relevant procurement regulations and data protection laws.

## Infrastructure

### Version Control

We will use the Github flow branching model for our repository, maintaining separate branches for features, releases, and hotfixes. Pull requests will be used for code review.

### Deployment

The application will be deployed on a cloud platform like AWS or Heroku. Continuous integration and deployment (CI/CD) pipelines will be set up for automated deployment.

### Data Population

Initially, we will provide sample data for testing purposes. For production, users will input their own procurement data through the application.

### Testing

We will use automated testing frameworks like PyTest for backend testing and Jest for frontend testing. Continuous integration will ensure that tests are run with every code push.

## Existing Solutions

- **SAP Ariba:** A comprehensive procurement management solution. ProcureIt aims to provide a simpler, more streamlined alternative, focusing on essential features for smaller organizations.

- **Coupa:** Another robust procurement platform. ProcureIt distinguishes itself by offering a more intuitive and user-friendly experience, catering to organizations that prefer simplicity over complexity.

## MVP Specification

### Architecture

[Insert Architecture Diagram]

### API and Methods

#### API Routes (Web Client to Server)

1. `POST /api/login`: Handles user authentication.
2. `GET /api/purchase_orders`: Retrieves a list of purchase orders.
3. `GET /api/purchase_orders/{id}`: Retrieves details of a specific purchase order.
4. `POST /api/goods_received_notes`: Creates a new Goods Received Note.
5. `GET /api/goods_received_notes`: Retrieves a list of Goods Received Notes.
6. `GET /api/goods_received_notes/{id}`: Retrieves details of a specific Goods Received Note.

#### Data Model

[Insert Entity Relationship Diagram (ERD)]

[Details of Tables and Relationships]

### User Stories

1. As a procurement manager, I want to be able to log in to the system so that I can access and manage purchase orders.

2. As a user, I want to view a list of purchase orders, so that I can see all pending and completed orders.

3. As a user, I want to view the details of a specific purchase order, so that I can review the order specifics and associated Goods Received Notes.

4. As a user, I want to create a Goods Received Note for a purchase order, including providing Delivery Note Numbers and Supplier Invoice Numbers.

5. As a user, I want to finalize a Goods Received Note and commit it to stock, marking the associated purchase order as completed.
