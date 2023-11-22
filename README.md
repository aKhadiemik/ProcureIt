# ProcureIt

ProcureIt is a procurement management application designed to simplify and streamline the procurement process for organizations. It enables efficient management of purchase requests, approvals, and vendor interactions.

## Intro
A demo of the app can be seen [here](https://youtu.be/ta3saQrKdZ4), this can also be accessed from the [project's landing page](https://akhadiemik.github.io/). [This blog](https://medium.com/@coagengo/the-journey-to-create-an-intuitive-application-for-procurement-workflows-5d147896b711) contains a brief writeup of the project. Connect with the author on [LinkedIn](https://www.linkedin.com/in/agengootieno/).

## Team

- C. Ageng`o – Software Architect and Full Stack Developer, UI/UX Designer

## Roles

- **Software Architect (Carlos Ageng`o):** Role - oversee the overall development process, handle project documentation, leads backend & frontend development, ensure an intuitive user experience.
  
- **User Interface and User Experience Design (Carlos Ageng`o):** Design user interfaces for simplicity and visual appeal.

## Technologies

### Backend

- Python (Django framework)
- MySQL database

### Frontend

- HTML
- CSS
- JavaScript

### Other Technologies

- Git for version control
- GitHub for collaboration and repository management

## Alternative Technology Choices

1. **Backend:** Django instead of Flask. Django  chosen for its extensibility, aligning better with the project's specific requirements.

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

Github flow branching model employed for this repository, maintaining separate branches for features, releases, and hotfixes. Pull requests used for code review.

### Deployment

The application built to be deployed either on-premise or over PaaS's platforms like AWS or Heroku. Continuous integration and deployment (CI/CD) pipelines set up for automated deployment.

### Requirements for Installation

The required packages for successful installation of the app are provided on the requirements.txt file. You will also need a web server - we recommend Nginx, for app server - gunicorn is recommended and for database server - MySQL. The app can be modified to work with any database server, however, you will require Python packages that allow for connection to those specific database servers.

In order for the application to work as desired ensure that the settings.py file is edited to work with the specific packages that you install.

### Usage

A great part of the paths to use the app is captured under User Stories here. You can create Supplier/Vendor Accounts, Create and Populate Purchase Orders, Create and Populate GRNs. The latter have to be linked to a specific Purchase Order.

### Data Population

Sample data used for testing purposes. For production, users will input their own procurement data through the application.

### Testing

Automated testing frameworks like PyTest uused for backend testing and Jest for frontend testing. Continuous integration to ensure that tests are run with every code push.

## Existing Solutions

- **SAP Ariba:** A comprehensive procurement management solution. ProcureIt aims to provide a simpler, more streamlined alternative, focusing on essential features for smaller organizations.

- **Coupa:** Another robust procurement platform. ProcureIt distinguishes itself by offering a more intuitive and user-friendly experience, catering to organizations that prefer simplicity over complexity.

## Related projects

Existing solutions above could be viewed as related projects. The team is however not responsible for any projects that are related to this. There are several applications in the market for Procurement management, the ones listed above do not exhaust the extent to which such apps are used in different organizations. 

## MVP Specification

### API and Methods

#### API Routes (Web Client to Server)

1. `POST /api/login`: Handles user authentication.
2. `GET /api/purchase_orders`: Retrieves a list of purchase orders.
3. `GET /api/purchase_orders/{id}`: Retrieves details of a specific purchase order.
4. `POST /api/goods_received_notes`: Creates a new Goods Received Note.
5. `GET /api/goods_received_notes`: Retrieves a list of Goods Received Notes.
6. `GET /api/goods_received_notes/{id}`: Retrieves details of a specific Goods Received Note.

### User Stories

1. As a procurement manager, I want to be able to log in to the system so that I can access and manage purchase orders.

2. As a user, I want to view a list of purchase orders, so that I can see all pending and completed orders.

3. As a user, I want to view the details of a specific purchase order, so that I can review the order specifics and associated Goods Received Notes.

4. As a user, I want to create a Goods Received Note for a purchase order, including providing Delivery Note Numbers and Supplier Invoice Numbers.

5. As a user, I want to finalize a Goods Received Note and commit it to stock, marking the associated purchase order as completed.

## Contributors

- C. Ageng`o

## Inspiration for Project

Having implemented ERP systems for clients in the past gave me an appreciation of the Procurement process within different organizations. The place of procurement in operations include ensuring that customer service levels are fulfilled and maintained at a high quality through:

1. the availability of goods required for provision of services to customers
2. the maintenance of auxiliary services which guarantee that business operations remain uninterrupted

In order to achieve this, it is necessary that sufficient budgetary allocations be made for what is to be procured. This requires that approvals be provided at specific points of the procurement workflow. User departments also have to conform to certain procedures.

The project's goal is to address one critical pain-point expressed by users. Provide a user friendly app that delivers reliable functionality to support the procurement process.

## Licensing

MIT License