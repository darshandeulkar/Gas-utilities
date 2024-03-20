# Gas-utilities
Django application to provide consumer services for gas utilities.
Gas Utilities Project is a Django-based web application designed to streamline gas utility management processes. It provides features for managing service requests, tracking status, and more.

## Features

- **Service Request Management**: Users can submit service requests for various gas utility needs such as installation, maintenance, and repairs.
- **Status Tracking**: Service providers can track the status of service requests, including pending, in progress, and completed.
- **Attachment Support**: Users can attach relevant documents or images to service requests for better clarification.
- **User Authentication**: Secure authentication system ensures that only authorized users can access and manage service requests.
- **Admin Panel**: Administrators have access to a dashboard for managing users, service requests, and other system settings.

- Below is the table structure
-----------------------------------------------------
| Table Name       | Fields                         |
|------------------|--------------------------------|
| Customer         | name (CharField)               |
|                  | email (EmailField)             |
|                  | phone_number (CharField)       |
|                  | address (TextField)            |
|                  | password (TextField)           |
-----------------------------------------------------
| ServiceRequest   | reqid (AutoField, Primary Key) |
|                  | service_type (CharField)       |
|                  | description (TextField)        |
|                  | attachment (FileField)         |
-----------------------------------------------------
| RequestStatus    | id (AutoField, Primary Key)    |
|                  | service_request (ForeignKey)   |
|                  | status (CharField)             |
|                  | updated_at (DateTimeField)     |
