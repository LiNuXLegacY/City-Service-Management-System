import uuid
from enum import Enum

# Enum for predefined service statuses
class ServiceStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    INACTIVE = "Inactive"
    IN_QUEUE = "In Queue"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    DECLINED = "Declined"

# Predefined service types
SERVICE_TYPES = [
    "Garbage Collection",
    "Water Supply",
    "Electricity Repair",
    "Road Maintenance",
    "Public Safety",
    "Appoint Public Meetings"
]

# Class to represent a single service request
class ServiceRequest:
    def __init__(self, request_id, name, address, service_type, description=None):
        self.request_id = request_id
        self.name = name
        self.address = address
        self.service_type = service_type
        self.description = description
        self.status = ServiceStatus.PENDING  # Default status is Pending
    def __str__(self):
        return f"""
        Request ID: {self.request_id}
        Name: {self.name}
        Address: {self.address}
        Service Type: {self.service_type}
        Description: {self.description or 'No description provided'}
        Status: {self.status.value}
        """

# Class to manage all client service requests
class CityService:
    def __init__(self):
        self.requests = []
    def generate_request_id(self):
        """ Generate a unique request ID """
        return str(uuid.uuid4())[:8]  # Generates an 8-character unique ID
    def add_request(self, name, address, service_type, description=None):
        """ Add a new service request """
        request_id = self.generate_request_id()
        new_request = ServiceRequest(request_id, name, address, service_type, description)
        self.requests.append(new_request)
        print(f"\nRequest added. Your Request ID: {request_id}")
    def view_pending_requests(self):
        """ Display all pending service requests """
        pending_requests = [request for request in self.requests if request.status == ServiceStatus.PENDING]
        if not pending_requests:
            print("\nNo pending service requests found.")
        else:
            print("\nPending Service Requests:")
            for request in pending_requests:
                print(request)
    def update_request_status(self, request_id):
        """ Update the status of a request """
        request = next((req for req in self.requests if req.request_id == request_id), None)
        if not request:
            print("Request ID not found.")
            return
        print("\nSelect a new status:")
        for index, status in enumerate(ServiceStatus, start=1):
            print(f"{index}. {status.value}")
        while True:
            try:
                status_choice = int(input("\nEnter the number for the new status: "))
                if 1 <= status_choice <= len(ServiceStatus):
                    request.status = list(ServiceStatus)[status_choice - 1]
                    print(f"Request ID {request_id} updated to {request.status.value}")
                    return
                else:
                    print(f"Invalid selection. Choose a number from 1 to {len(ServiceStatus)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Main Program
def main():
    city_service = CityService()

    while True:
        print("\nCity Service Management System")
        print("1. Add Service Request")
        print("2. View Pending Requests")
        print("3. Update Request Status")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            if choice == 1:
                while True:
                    name = input("\nEnter the person's name: ").strip()
                    address = input("Enter the address: ").strip()
                    if not name or not address:
                        print("Name and address cannot be empty. Please try again.")
                        continue
                    selected_services = []

                    # Multi-service selection loop
                    while True:
                        # Display available service types
                        print("\nAvailable Service Types:")
                        for index, service in enumerate(SERVICE_TYPES, start=1):
                            print(f"{index}. {service}")
                        print("Type 'exit' if you are done selecting service types.")
                        # Validate user input for service type
                        service_choice = input(
                            "\nEnter the number corresponding to your chosen service type (or type 'exit' to finish): ").strip()
                        if service_choice.lower() == "exit":
                            break
                        try:
                            service_choice = int(service_choice)
                            if 1 <= service_choice <= len(SERVICE_TYPES):
                                service_type = SERVICE_TYPES[service_choice - 1]
                                selected_services.append(service_type)
                                print(f"Service '{service_type}' added to your request.")
                            else:
                                print(f"Invalid choice. Please enter a number from 1 to {len(SERVICE_TYPES)}.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number or type 'exit'.")

                    if not selected_services:
                        print("No services selected. Please try again.")
                        continue
                    # Prompt for a description
                    description = input("Enter a brief description of the issue (optional): ").strip()

                    # Add each selected service request for this person
                    for service_type in selected_services:
                        city_service.add_request(name, address, service_type, description)

                    # Ask if the user wants to enter another request
                    another_entry = input("\nWould you like to add another request? (yes/no): ").strip().lower()
                    if another_entry != "yes":
                        break

        elif choice == 2:
            city_service.view_pending_requests()
        elif choice == 3:
            request_id = input("\nEnter Request ID to update: ")
            city_service.update_request_status(request_id)
        elif choice == 4:
            print("\nExiting the system. Goodbye.")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 4.")


# Run the program
if __name__ == "__main__":
    main()