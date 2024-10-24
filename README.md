# MeraTutor

![Logo](./images/tutor.jpeg)

[![License](https://img.shields.io/badge/License-Apache2-blue.svg)]
(https://www.apache.org/licenses/LICENSE-2.0)
## Contents
1. [Short Description](#short-description)
1. [Demo Video](#demo-video)
1. [The Architecture](#architecture-overview)
1. [Long Description](#long-description)
1. [Project Roadmap](#project-roadmap)
1. [Live demo](#live-demo)
1. [Built With](#built-with)
1. [The Team](#team)
1. [License](#license)

## Short Description 

**MeraTutor** - AI-powered virtual teacher ensures continuous, personalized learning remotely.

### Problem Statement

The current education system, while robust in many ways, often fails to address the individual learning needs of students. Major challenges include:

* **Inequitable Access**: Students from underserved communities or those with disabilities often don’t get the personalized resources or support they need to help with their learning challenges. This leads to learning gaps and missed opportunities for success.

* **Climate Change** : Natural disasters like floods, droughts, wildfires etc, made worse by climate change disturb education by damaging schools, forcing families to move, and causing temporary school closures. Vulnerable communities are hit the hardest, making it harder for kids to continue their education.

* **Transportation Barriers**: In remote areas, students struggle to reach schools because of long distances, poor roads, or lack of affordable transport. Disasters like floods or landslides make getting to school even harder.

* **Lack of Personalized Learning**: Many students find it difficult to keep up in traditional classrooms because lessons aren’t designed to match their learning pace or style.
    
* **Resource Constraints**: Teachers often have large class sizes and limited time, making it hard to give each student the individual attention they need.
    
* **Assessment Gaps**: Traditional assessments don’t offer immediate feedback on how well a student understands a topic and fail to adapt to individual learning needs.

### How can technology help?

MeraTutor helps students continue learning, even when they can't go to school because of problems like natural disasters, bad weather, or transportation issues. It adjusts lessons to fit each student’s way of learning and how fast they learn, so no one falls behind. If schools are closed or students can’t attend in person, it lets them learn from home or anywhere else. It makes learning fun by using interactive activities, quizzes, and games, and gives instant feedback so students know how they’re doing right away.

It also supports students with special learning needs by giving personalized attention and lessons that are easier to understand. It acts like a tutor, offering assignments, asking questions, and giving helpful feedback to keep students on track. If a student struggles with a topic, the virtual tutor can re-explain it in a simpler way. By providing continuous and tailored learning, MeraTutor make sure students don’t miss out on education, even during difficult situations, and helps them stay motivated and engaged in their studies.

### The idea

**AI-Powered Learning Assistants for Inclusive Education**

To solve the problems of personalizing education and making it accessible for all students, we are proposing an innovative AI-powered learning system that acts like a personal tutor for every student. This system has three intelligent agents that work together to create a well-rounded learning experience tailored to individual needs.

* **Virtual Tutor**: This assistant acts like a friendly teacher. It explains lessons in a way that’s easy to understand and answers any questions students might have. If a student is struggling with a topic, the Virtual Tutor changes its explanations to fit the student’s level of understanding. This ensures that no student feels lost or left behind, allowing everyone to learn at their own pace.
* **Quiz Generator**: To make students feel confident in what they’ve learned, it can create quizzes to test their knowledge. These quizzes are not one-size-fits-all; they adapt to focus on the specific topics that each student has studied. This means students can practice what they need to work on most, making studying more effective and relevant to their learning journey.
* **Evaluator & Feedback Agent**: After students complete a quiz, this agent evaluates their answers and provides detailed feedback. It highlights what the student did well and points out areas where they might need more practice. Additionally, it generates a report that gives a clear overview of the student’s performance, offering helpful suggestions for improvement. This way, students receive constructive feedback that guides them on what to focus on next.
  
This AI-powered learning system personalizes the educational experience for every student, ensuring equitable access to quality education. It continuously adapts to each student’s progress. By acting as a personal tutor, this system empowers all students, regardless of their background or learning challenges, to reach their full potential and thrive in their educational journey.

### IBM AI service(s) used
- [IBM Watsonx Prompt Lab (with Granite-20B Multilingual foundational model)](https://www.ibm.com/watsonx?utm_content=SRCWW&p1=Search&p4=43700076605828901&p5=e&gclid=CjwKCAjwysipBhBXEiwApJOcuz1PY3AhyOywNZ75iQZFK1tdjMKvi0V0VIvdY_qeas-M7QReiaDpixoCI2AQAvD_BwE&gclsrc=aw.ds) - IBM Watsonx Prompt Lab, which uses the Granite-20B Multilingual model, powers our AI virtual tutor. It helps the virtual tutor understand and answer student questions in different languages. This means students get explanations that fit their understanding, no matter their language or background.
- [IBM Watson Speech to Text](https://cloud.ibm.com/catalog/services/spech-to-text) - Watson Speech to Text changes spoken words into written text. We used this feature so students can talk to the virtual tutor and also the tutor lecture will be converted to text for reference to student. This makes learning easier for students who have visual impairments or prefer speaking instead of typing.
- [IBM Watson Machine learning](https://cloud.ibm.com/catalog/services/watson-machine-learning)
  We used IBM Watson Machine Learning to run and manage our AI models that help the learning system work effectively. This tool allows us to create personalized responses, quizzes, and feedback for students, making sure the system adapts to each student's needs.

### Other IBM technology used
- [Cloud Object Storage](https://cloud.ibm.com/objectstorage/create?catalog_query=aHR0cHM6Ly9jbG91ZC5pYm0uY29tL2NhdGFsb2c%2FY2F0ZWdvcnk9c3RvcmFnZSNzZXJ2aWNlcw%3D%3D)
This service helped us to store our models and provided the expected scalability in a seamless way along with greater resiliency and make secure storage for data, allowing us to store educational resources and multimedia content efficiently

### Demo video

[![Demo](./images/tutor.jpeg)](https://www.youtube.com/watch?v=7Wijl7lTYAI "MeraTutor")

For GitHub use CTRL+click (on Windows and Linux) or CMD+click (on MacOS) on the link to open in new window.
Please click on the image to view the video on YouTube.

### Architecture Overview

![Architecture](./images/arch.jpeg)

1. Student ingests the books and study material into the MeraTutor. Also he sets the parameters to personalize his learning. 

2. The student then asks the question

3. Based on the question the appropriate SME (AI agent) is called to answer the question. 

4. These AI agents get their power from IBM watsonx LLM

5. After that, the student can use another AI agent to play a Quiz to check his knowledge. The agent also provides score and feedback based on the answers

6. The Student can finally find assignments that are created based on the concepts he learned.

### Long Description

MeraTutor is a smart AI-powered virtual teacher designed to help students learn in a way that fits their needs, making education accessible for everyone. It aims to solve the problems in the current education system, especially for students from underserved communities or those with special needs, by providing a personalized learning experience that adapts to each student’s situation.

By leveraging the power of AI and technology, our solution(MeraTutor) aims to bridge the educational divide, ensuring that students in vulnerable communities receive the quality education they deserve. This solution not only helps prevent learning loss during critical times but also empowers students to take control of their learning journey. Ultimately, we envision a future where every child, regardless of their circumstances, has access to engaging, personalized, and effective education, enabling them to thrive academically and beyond.

Our solution(MeraTutor) centers around an innovative AI-powered virtual teacher designed to address the educational disruptions faced by students in vulnerable communities, particularly those impacted by climate change, conflict, or economic hardship. This virtual teacher provides a dynamic and interactive learning experience that ensures continuous education, even when students cannot physically attend school.


**Key Features of Our Solution**:

**Personalized Learning Experience**: The virtual teacher tailors lessons to each student’s individual learning style and pace. By analyzing responses and performance data, it identifies areas where students may struggle and adapts the content accordingly. This personalization helps ensure that all students grasp the material, regardless of their starting point.

**Interactive and Engaging Content**: Learning is made enjoyable through a variety of interactive activities, including quizzes. This kind of approach keeps students motivated and engaged, encouraging them to participate actively in their education.

**Continuous Access to Education**: With our virtual teacher, students can access learning materials anytime and anywhere, overcoming barriers posed by school closures or geographic isolation. This flexibility allows them to continue their studies at their convenience, ensuring they don’t fall behind.

**Feedback and Assessment**: The virtual teacher provides immediate feedback on assignments/quizzes, helping students understand their mistakes and learn from them. This instant feedback loop fosters a growth mindset and encourages continuous improvement.


**Content Adaptation for Understanding**: If a student struggles with a topic, the virtual teacher can deliver the same lesson in a different, more comprehensible manner. It can present information using various formats, such as videos, diagrams, or simplified explanations, catering to diverse learning preferences.

**Assignments and Reinforcement**: After each lesson, the virtual teacher provides relevant assignments/quizzes tailored to reinforce what students have learned. These tasks help solidify knowledge and ensure that students can apply their understanding in practical contexts.

**Culturally Relevant Materials**: We emphasize inclusivity by integrating culturally relevant content and materials that resonate with the students' backgrounds, making learning more relatable and meaningful.

**Emergency Preparedness**: Our solution includes features that allow for updates and adjustments in the curriculum in response to emergency situations, ensuring that education can continue despite external challenges.
    
    
    
**How MeraTutor Works**

MeraTutor includes several smart features that work together to enhance learning:

**Virtual Tutor**: This friendly assistant explains lessons clearly and answers questions in their regional language if needed. It adapts its explanations based on each student’s understanding, ensuring everyone feels supported in their learning.

**Quiz Generator**: When students feel ready, MeraTutor creates personalized quizzes to test their knowledge. These quizzes help reinforce what they’ve learned and identify areas where they need more practice.

**Evaluator & Feedback Agent**: After quizzes, students get detailed feedback on their answers. This agent highlights what they did well and points out where they can improve, giving them useful insights for their learning.

**Continuous Learning**: MeraTutor keeps track of how each student is doing and adjusts its approach to provide ongoing support. If a student struggles with a topic, the Virtual Tutor can explain it again in a simpler way, making sure they understand before moving on.

MeraTutor makes learning fun and engaging through interactive activities. By offering personalized attention and continuous support, it helps students stay motivated and connected, no matter their circumstances.

MeraTutor aims to create a fairer education system where every student has the chance to learn, grow, and succeed. By using technology to provide customized learning experiences, MeraTutor helps students overcome challenges and reach their full potential in their educational journeys.


### Project roadmap
![Roadmap](./images/Roadmap.jpeg)

### Built with
![Techonology](./images/arch1.jpeg)

### Getting started

### Setup

This code works on Python3+ versions.

### Clone the repository

## With Docker:

$ git clone https://github.com/MeraTutor/MeraTutor-Webapp.git

$ MeraTutor-Webapp/

## Install Docker
https://docs.docker.com/engine/install/ubuntu/

## Build docker image

$ docker build -t aitutor_docker .

Note: ensure in app.py port is mentiond as 8080

$ docker run -it -p 8080:8080 aitutor_docker

In Browser run with 127.0.0.1:8080

## To push:

$docker login

  Username: XXXX
  
  Password: XXXX
  
$ docker tag aitutor_docker aitutor/aitutor_docker:1.0.0

$ docker push aitutor/aitutor_docker:1.0.0

## Without Docker:

## Install the required libraries

$ pip3 install -r requirements.txt

## Clone the repository

$ git clone https://github.com/MeraTutor/MeraTutor-Webapp.git

$ MeraTutor-Webapp/

## Run app.py

$ python3 app.py 

or

$ python -m flask run

In Browser run with 127.0.0.1:5000


### Live Demo
[MeraTutor Demo Link](http:///)


### Team

- [Suneetha Jonnadula](https://github.com/Sunivihaan) - _Lead Full Stack developer_
- [Prashanth P](https://github.com/Prashanthp) - _Principal Application developer_
- [Mohamed Fazil](https://github.com/Fazil-24) - _AI / ML Development Engineer_
- [Bharathi Athinarayanan](https://github.com/rathisoft) - AI / ML architect_ 

### License
This project is licensed under the Apache 2 License - see the [LICENSE](LICENSE) file for details.

