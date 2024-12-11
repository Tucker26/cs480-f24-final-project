# Requirements Analysis Document
### Project Description
This project is a file storage system that implements file upload, file download, and list stored files microservices.
### Functional Requirements
1. Upload file
   * Upload local file to cloud storage given file path
   * If file path is invalid, return error
2. List stored files
   * Return list of file names in cloud storage
3. Download file
   * Download file from cloud storage given file path
### Technical Architecture
#### Microservices
1. POST API Upload
2. GET API List
3. GET API Download