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
1. Upload API
   * POST request
2. List API
   * GET request
3. Download API
   * GET request