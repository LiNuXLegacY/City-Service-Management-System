Title: “City Services Management System”
Focus: Simple Object-Oriented Programming (OOP) concepts and Data Structures applied to daily city applications.
Programming Environment: Python in VS Code/PyCharm (no external extensions or libraries installed).

Overview:

This Python program is a City Service Management System that allows users to submit, track, and update service requests. It is built using object-oriented programming (OOP) principles and incorporates essential features for managing city services.

Main Components:

Service Request Management:
- Users can create service requests by providing their name, address, service type, and an optional description.
- Each request gets a unique ID generated using the uuid module.

Service Status Handling:
- The program defines predefined statuses using an Enum (ServiceStatus) to ensure consistency across requests.
- Users can update request statuses such as Pending, In Progress, Completed, Cancelled, etc.

List-Based Storage: 
- All requests are stored in a list (self.requests), allowing easy retrieval and modification.

User Interaction:
- A menu-driven system guides users through the following options:
- Adding a new service request (supports multi-service selection).
- Viewing pending service requests.
- Updating request status.
- Exiting the program.

Applications:
This project provides an efficient way to manage city service requests, ensuring that requests are properly logged, tracked, and updated based on user input. By leveraging object-oriented programming and enums, the system maintains well-structured and scalable service management.

