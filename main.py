from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

courses = [
    {
        "id": 1,
        "name": "Intro to Python",
        "description":
        "Learn the basics of Python, a popular programming language for both beginners and experts.",
        "category": "Programming Fundamentals",
        "video_src": {
            "intro":
            "https://www.youtube.com/embed/xkZMUX_oQX4?si=rFcZhc3GcgYDljRx",
        },
        "image_src":
        "https://images.unsplash.com/photo-1649180556628-9ba704115795?q=80&w=2062&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "lectures": {
            "lecture1": {
                "title":
                "Introduction to Python",
                "video_src":
                "https://www.youtube.com/embed/xkZMUX_oQX4?si=lOmrTCNbimwB9eQS",
            },
            "lecture2": {
                "title":
                "Get Started",
                "video_src":
                "https://www.youtube.com/embed/z116jFWdfQc?si=TEsHpfwRbOt1kd3v",
            },
            "lecture3": {
                "title":
                "Basic Syntax and Data Types",
                "video_src":
                "https://www.youtube.com/embed/4WVZBtqqVM4?si=uSiaWXFIAnA0qW1G"
            },
            "lecture4": {
                "title": "Homework"
            }
        },
        "duration": "1-2 hours",
        "review": "4.9/5"
    },
    {
        "id": 2,
        "name": "Advanced Python",
        "description":
        "Discover Python's power in data analysis and visualization for data science projects.",
        "category": "Programming Fundamentals",
        "video_src": {
            "intro":
            "https://www.youtube.com/embed/Gf9wLsCJDqc?si=Lj-vkmuPIlGHHPYm",
        },
        "image_src":
        "https://images.unsplash.com/photo-1690683789978-3cf73960d650?q=80&w=1809&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "lectures": {
            "lecture1": {
                "title":
                "Variables and Operators",
                "video_src":
                "https://www.youtube.com/embed/Gf9wLsCJDqc?si=Lj-vkmuPIlGHHPYm",
            },
            "lecture2": {
                "title":
                "Assign Multiple Values to Variables",
                "video_src":
                "https://www.youtube.com/embed/4oug4GEDSeM?si=zrzekamLIWnAisiI",
            },
            "lecture3": {
                "title":
                "Global Variables",
                "video_src":
                "https://www.youtube.com/embed/VZW9CGZymqU?si=Dc8aSJIRPR1NIu2-"
            },
            "lecture4": {
                "title": "Homework"
            }
        },
        "duration": "2-3 hours",
        "review": "4.8/5"
    },
    {
        "id": 3,
        "name": "HTML for Beginners",
        "description":
        "Learning how to structure web pages by using HTML for beginner.",
        "category": "Web Development",
        "video_src": {
            "intro":
            "https://www.youtube.com/embed/it1rTvBcfRg?si=--fXeKHW5gndsKT6",
        },
        "image_src":
        "https://a.storyblok.com/f/42126/0b0046053d/html-beginners-guide.png/m/1600x900/filters:quality(70)/",
        "lectures": {
            "lecture1": {
                "title":
                "HTML Elements",
                "video_src":
                "https://www.youtube.com/embed/vIoO52MdZFE?si=LxPljrj1dh5pR2QZ",
            },
            "lecture2": {
                "title":
                "HTML Attributes ",
                "video_src":
                "https://www.youtube.com/embed/yMX901oVtn8?si=DrvKYlT17oSB0E2N",
            },
            "lecture3": {
                "title":
                "HTML Formatting",
                "video_src":
                "https://www.youtube.com/embed/7FqQLqNIEY8?si=TwPF7Ea2a4LImt_v"
            },
            "lecture4": {
                "title": "Homework"
            }
        },
        "duration": "1-2 hours",
        "review": "4.9/5"
    },
    {
        "id": 4,
        "name": "Advanced HTML",
        "description":
        "Dive deeper into HTML to learn advanced concepts like table, form and style with CSS",
        "category": "Web Development",
        "video_src": {
            "intro":
            "https://www.youtube.com/embed/cZHp-Oozg6I?si=sc8zSZwAMExnZppF",
        },
        "image_src":
        "https://img.freepik.com/free-photo/programming-background-collage_23-2149901782.jpg?t=st=1733217133~exp=1733220733~hmac=75270fa4fd7b54a8f3555358d3ba0756488f4be63861e31bbeb9e6b5a9322084&w=996",
        "lectures": {
            "lecture1": {
                "title":
                "HTML with CSS",
                "video_src":
                "https://www.youtube.com/embed/cZHp-Oozg6I?si=fQ8Rj-zXIGxlAwoL",
            },
            "lecture2": {
                "title":
                "HTML Table ",
                "video_src":
                "https://www.youtube.com/embed/e62D-aayveY?si=ItJ1T5tYgW83defL",
            },
            "lecture3": {
                "title":
                "HTML Forms",
                "video_src":
                "https://www.youtube.com/embed/VLeERv_dR6Q?si=0RvRZxQR02_NJGJq"
            },
            "lecture4": {
                "title": "Homework"
            }
        },
        "duration": "1-2 hours",
        "review": "4.8/5"
    },
    {
        "id": 5,
        "name": "Basic CSS for Beginners",
        "description":
        "Learn the basics of CSS to style and format web pages, making them visually appealing",
        "category": "Web Development",
        "video_src": {
            "intro":
            "https://www.youtube.com/embed/AGDDdsiZ0Ko?si=9NI5Je3VMM2bweYW",
        },
        "image_src":
        "https://resources.reed.co.uk/courses/coursemedia/447476/e8585418-d6ec-4e6b-99db-d8b20bafd245_cover.webp",
        "lectures": {
            "lecture1": {
                "title":
                "CSS Introduction",
                "video_src":
                "https://www.youtube.com/embed/AGDDdsiZ0Ko?si=9NI5Je3VMM2bweYW",
            },
            "lecture2": {
                "title":
                "CSS Syntax ",
                "video_src":
                "https://www.youtube.com/embed/G8r00ZNopTE?si=I9fKU4AFvbJs8Qeu",
            },
            "lecture3": {
                "title":
                "How to add CSS to HTML",
                "video_src":
                "https://www.youtube.com/embed/VSwaoQ3TFkQ?si=tvrpp48HsNaTVqIi"
            },
            "lecture4": {
                "title": "Homework"
            }
        },
        "duration": "1-2 hours",
        "review": "4.8/5"
    },
    {
        "id": 6,
        "name": "Advanced JavaScript",
        "description":
        "Take your JavaScript skills to the next level with this advanced course.",
        "category": "Web Development",
        "video_src": {
            "intro":
            "https://www.youtube.com/embed/uSgcWDkwc3U?si=4NrDS61WgultWFWJ"
        },
        "image_src":
        "https://img.freepik.com/free-vector/programmers-using-javascript-programming-language-computer-tiny-people-javascript-language-javascript-engine-js-web-development-concept-bright-vibrant-violet-isolated-illustration_335657-986.jpg?t=st=1733220340~exp=1733223940~hmac=6b8e2693d983bb26b99ce04e373b4a6d20a2b396c00f609164faad1fb9f173be&w=996",
        "lectures": {
            "lecture1": {
                "title":
                "JavaScript Variables ",
                "video_src":
                "https://www.youtube.com/embed/P1abmTnje_8?si=TbmOuw3WyITjmZCv",
            },
            "lecture2": {
                "title":
                "Operators and Functions",
                "video_src":
                "https://www.youtube.com/embed/PvAxzOBZnas?si=XYrdKWTPhBBFScNZ",
            },
            "lecture3": {
                "title":
                "Classes in Javascript",
                "video_src":
                "https://www.youtube.com/embed/iqjfck9Hj6g?si=jjtgaQw9m3QVgEX1"
            },
            "lecture4": {
                "title": "Homework"
            }
        },
        "duration": "3-4 hours",
        "review": "5/5"
    },
    {
        "id": 7,
        "name": "Machine Learning with TensorFlow",
        "description":
        "Learn how to build machine learning models using the popular TensorFlow library.",
        "category": "Machine Learning",
        "video_src": {
            "intro":
            "https://www.youtube.com/embed/MrijcdNl_U4?si=3iLpFBNejPs-wIJj"
        },
        "image_src":
        "https://skillxprss.com/wp-content/uploads/2021/02/machine-learning-3.jpg",
        "lectures": {
            "lecture1": {
                "title":
                "Introduction to TensorFlow",
                "video_src":
                "https://www.youtube.com/embed/MotG3XI2qSs?si=mSwf8wJcOQByNlY4",
            },
            "lecture2": {
                "title":
                "What Is Machine Learning?",
                "video_src":
                "https://www.youtube.com/embed/ukzFI9rgwfU?si=P6WfInwATSCrVjvR",
            },
            "lecture3": {
                "title":
                "AI & Machine Learning with TensorFlow",
                "video_src":
                "https://www.youtube.com/embed/wnqkfpCpK1g?si=aXI6o8OwSwdsl77_"
            },
            "lecture4": {
                "title": "Homework"
            }
        },
        "duration": "8-9 hours",
        "review": "4.7/5"
    },
    {
        "id": 8,
        "name": "Deep Learning Basics",
        "description":
        "Dive into deep learning concepts and build simple models using TensorFlow.",
        "category": "Machine Learning",
        "video_src": {
            "intro":
            "https://www.youtube.com/embed/E8n_k6HNAgs?si=-xnhmsAaXdvOTaRV"
        },
        "image_src":
        "https://cdn.pixabay.com/photo/2024/01/29/22/47/ai-generated-8540915_1280.jpg",
        "lectures": {
            "lecture1": {
                "title":
                "What is TensorFlow",
                "video_src":
                "https://www.youtube.com/embed/E8n_k6HNAgs?si=-xnhmsAaXdvOTaRV",
            },
            "lecture2": {
                "title":
                "TensorFlow Tutorial For Beginners",
                "video_src":
                "https://www.youtube.com/embed/LP59LkH6tzs?si=Zgfp9vTwP1mKLSl4",
            },
            "lecture3": {
                "title":
                "Deep Learning with TensorFlow",
                "video_src":
                "https://www.youtube.com/embed/_NMI8peAmNA?si=xQ6AH8pOhYGfzE6O"
            },
            "lecture4": {
                "title": "Homework"
            }
        },
        "duration": "6-7 hours",
        "review": "4.9/5"
    },
    {
        "id": 9,
        "name": "Data Science with R",
        "description":
        "Explore the world of data science using the R programming language.",
        "category": "Data Science",
        "video_src": {
            "intro":
            "https://www.youtube.com/embed/X3paOmcrTjQ?si=lPviJpDlK5XkiCgV"
        },
        "image_src":
        "https://img.freepik.com/free-vector/illustration-social-media-concept_53876-18140.jpg?t=st=1733223011~exp=1733226611~hmac=81d7c6e9b001d0de42f3701a45a68d07302de68c254988c952f058b617e5d225&w=1060",
        "lectures": {
            "lecture1": {
                "title":
                "What Is Data Science?",
                "video_src":
                "https://www.youtube.com/embed/X3paOmcrTjQ?si=2hdUziq1idOgnPKB",
            },
            "lecture2": {
                "title":
                "R Programming For Beginners",
                "video_src":
                "https://www.youtube.com/embed/Uenf8DbOjz0?si=umw9fE4pOr72NX4m",
            },
            "lecture3": {
                "title":
                "Data Science With R",
                "video_src":
                "https://www.youtube.com/embed/Zi0cfo5CHRM?si=LJW37pdEvAbjck3m"
            },
            "lecture4": {
                "title": "Homework"
            }
        },
        "duration": "4-5 hours",
        "review": "5/5"
    },
    {
        "id": 10,
        "name": "Basic SQL",
        "description":
        "Learn the essentials of SQL, including querying, filtering, and managing data in relational databases.",
        "category": "Data Science",
        "video_src": {
            "intro":
            "https://www.youtube.com/embed/zpnHsWOy0RY?si=kd6y2Dxmy2ByXmsD"
        },
        "image_src":
        "https://img.freepik.com/free-vector/abstract-technology-sql-illustration_23-2149237139.jpg?t=st=1733226453~exp=1733230053~hmac=9f19e5ab8eb5747e6bf752dc029d0ec73076b73a361e48b866cd0b37e4288530&w=740",
        "lectures": {
            "lecture1": {
                "title":
                "SQL Introduction",
                "video_src":
                "https://www.youtube.com/embed/zpnHsWOy0RY?si=Oq_KaQunfEexB1HL",
            },
            "lecture2": {
                "title":
                "SELECT Statement ",
                "video_src":
                "https://www.youtube.com/embed/af4LckivJT8?si=JmFqMByEeLSWyg91",
            },
            "lecture3": {
                "title":
                "DELETE Statement",
                "video_src":
                "https://www.youtube.com/embed/s7ehCYyEmVw?si=QmJ0Lza5qTYwb4GS"
            },
            "lecture4": {
                "title": "Homework"
            }
        },
        "duration": "1-2 hours",
        "review": "4.9/5"
    },
]


@app.route('/')
def index():
    return "<h1>Final API</h1><br>สำหรับวิธีการเข้าใช้งาน API สามารถเข้าใช้งานได้ดังนี้ <br><li><b>การเข้าถึงรายละเอียดแต่ละคอร์ส</b> สามารถเข้าได้ที่ /courses/<int:course_id> โดย course_id คือ ไอดีของแต่ละหลักสูตร<br>เช่น https://borntodev-final-project-api.borntodev.repl.co/courses/1</li><li><b>ดูรายการหลักสูตรทั้งหมด</b> สามารถเข้าได้ที่ /courses จะแสดงข้อมูลหลักสูตรทั้งหมดออกมา<br>เช่น https://borntodev-final-project-api.borntodev.repl.co/courses</li><li><b>ดูรายการหมวดหมู่ทั้งหมด</b> สามารถเข้าได้ที่ /categories จะแสดงชื่อหมวดหมู่ทั้งหมดออกมา<br>เช่น https://borntodev-final-project-api.borntodev.repl.co/categories</li><li><b>ดูรายการหมวดหมู่ทั้งหมด</b> สามารถเข้าได้ที่ /categories/<string:category_name>/courses โดยเราจะใส่ชื่อหมวดหมู่ลงไป เราจะได้หลักสูตรทั้งหมดในหมวดหมู่นั้น ๆ ออกมา<br>เช่น https://borntodev-final-project-api.borntodev.repl.co/categories/Web%20Development/courses (ตัวพิมพ์เล็ก และ ใหญ่มีผล)</li><p>ขอให้ทุกคนพยายามอย่างเต็มที่กับ Project Final ของหลักสูตรนี้นะครับ 😊</p>"


@app.route('/courses', methods=['GET'])
def get_all_courses():
    return jsonify(courses)


@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = next((course for course in courses if course["id"] == course_id),
                  None)
    if course is not None:
        return jsonify(course)
    else:
        return jsonify({"message": "Course not found"}), 404


@app.route('/categories', methods=['GET'])
def get_categories():
    categories = list(set(course['category'] for course in courses))
    return jsonify(categories)


@app.route('/categories/<string:category_name>/courses', methods=['GET'])
def get_courses_in_category(category_name):
    category_courses = [
        course for course in courses if course["category"] == category_name
    ]
    if category_courses:
        return jsonify(category_courses)
    else:
        return jsonify({"message": "No courses found in this category"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
