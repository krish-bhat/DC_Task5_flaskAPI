## DC_Task5_flaskAPI

what is this API?

The provided Flask application (app.py) offers a robust solution for file uploads and retrieval. It seamlessly integrates web-based file uploading with RESTful API capabilities, catering to both user-driven interactions and programmatic access. With a user-friendly HTML interface, users can conveniently select and upload multiple files of various formats. Meanwhile, the application's API endpoints enable seamless integration with other systems, facilitating automated file uploads and metadata retrieval. Leveraging MongoDB for efficient storage and retrieval of file metadata enhances scalability and data management. This application serves as a versatile tool for handling file-related tasks, whether for interactive web use or backend integration within larger systems, offering flexibility and efficiency in managing file uploads and associated information.

# How to install this  

Organization or your repository

![image](https://github.com/krish-bhat/DC_Task5_flaskAPI/assets/99545739/6d9930c2-000a-47d0-9cf4-5f905d239c27)

Create a virtual environment (optional), and make sure it has :

pip install Flask,
  pip install pymongo, 
   pip install Werkzeug

There is mongodb connection that is made which collects the file metadata 

make sure to add an 'uploads' folder 

after, run app.py click on http://127.0.0.1:5000 (the link which is been mentioned that is been hosted) to load the files

![image](https://github.com/krish-bhat/DC_Task5_flaskAPI/assets/99545739/58fc63f1-80dc-4595-b874-353cb1094b65)


# Screenshots (browser)
![image](https://github.com/krish-bhat/DC_Task5_flaskAPI/assets/99545739/202d93ae-c83b-46f4-bf22-56f9820751fd)

![image](https://github.com/krish-bhat/DC_Task5_flaskAPI/assets/99545739/90d85f53-75ca-404d-aaca-d5f43507f6c7)

![image](https://github.com/krish-bhat/DC_Task5_flaskAPI/assets/99545739/33e5ff4a-bdf7-4c44-995c-aa5ac8584b43)

# Screenshots (mongodb collection)
![image](https://github.com/krish-bhat/DC_Task5_flaskAPI/assets/99545739/d5f2ef08-3ebe-41ef-b0a7-889d719159a1)

![image](https://github.com/krish-bhat/DC_Task5_flaskAPI/assets/99545739/68ccd233-b470-42cd-9db3-7a30c514364a)

![image](https://github.com/krish-bhat/DC_Task5_flaskAPI/assets/99545739/5853855a-1d3c-4693-a073-2f9c5e48f458)

The uploaded files are seen in 'uploads' folder

