import os
import shutil

# Task 17: Create images directory and move images
os.makedirs('rescue/images', exist_ok=True)
for img in ['baby-raccoons.jpg', 'tortoise.jpg']:
    src = f'resources/{img}'
    dst = f'rescue/images/{img}'
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f'Copied {img} to rescue/images/')

# Task 02-04: Update template.html
template_html = '''<!-- Write your code here --><!DOCTYPE html>
<!--
    Student Name: Mike Dahlin
    File Name: template.html
    Date: 06/22/2026
-->
<html lang="en">
    <head>
        <title>Wild Rescues: Template</title>
        <meta charset="utf-8">
    </head>
    <body>

        <header>
            <h1>&#128062; Wild Rescues</h1>
            <h3>Rescue. Rehabilitate. Release.</h3>
        </header>

        <nav>
            <p><a href="index.html">Home</a> &nbsp; &#9672; &nbsp;
<a href="about.html">About Us</a> &nbsp; &#9672; &nbsp;
<a href="partnership.html">Partnership</a> &nbsp; &#9672; &nbsp;
<a href="gallery.html">Gallery</a> &nbsp; &#9672; &nbsp;
<a href="faqs.html">FAQs</a> &nbsp; &#9672; &nbsp;
<a href="contact.html">Contact</a></p>
        </nav>

        <!-- Use the main area to add the main content to the webpage -->
        <main>
            <div></div>
        </main>

        <footer>
            <p>&copy; Copyright 2021. All Rights Reserved.</p>
            <p><a href="mailto:contact@wildrescues.net">contact@wildrescues.net</a></p>
        </footer>

    </body>
</html>'''

with open('rescue/template.html', 'w') as f:
    f.write(template_html)
print('Updated template.html')

# Tasks 02, 04, 05, 06, 07, 08, 09: Update index.html
index_html = '''<!-- Write your code here --><!DOCTYPE html>
<!--
    Student Name: Mike Dahlin
    File Name: index.html
    Date: 06/22/2026
-->
<html lang="en">
    <head>
        <title>Wild Rescues: Home</title>
        <meta charset="utf-8">
    </head>
    <body>

        <header>
            <h1>&#128062; Wild Rescues</h1>
            <h3>Rescue. Rehabilitate. Release.</h3>
        </header>

        <nav>
            <p><a href="index.html">Home</a> &nbsp; &#9672; &nbsp;
<a href="about.html">About Us</a> &nbsp; &#9672; &nbsp;
<a href="partnership.html">Partnership</a> &nbsp; &#9672; &nbsp;
<a href="gallery.html">Gallery</a> &nbsp; &#9672; &nbsp;
<a href="faqs.html">FAQs</a> &nbsp; &#9672; &nbsp;
<a href="contact.html">Contact</a></p>
        </nav>

        <main>
            <div id="welcome">
                <p>Welcome to Wild Rescues. Our mission is to rescue, rehabilitate, and release wildlife back into their natural environment. We are a nonprofit organization dedicated to helping injured wildlife.</p>

                <p>Our staff provides around-the-clock care for wildlife in need. We also provide long-term care for wildlife that cannot be released back into their natural environment.</p>

                <p>Will you partner with us? We need caring volunteers to help care for our animals. You can also donate, become a member, or become a sponsor. Contact us today.</p>
            </div>

            <div id="latest">
                <h2>Our Latest Rescue: Baby Raccoons</h2>
                <img src="images/baby-raccoons.jpg" alt="hands holding three baby raccoons" height="330" width="500">
                <p>Meet our latest rescues, Fizz, Bandit, and Mohawk. These three little guys were found abandoned near a home.</p>
            </div>
        </main>

        <footer>
            <p>&copy; Copyright 2021. All Rights Reserved.</p>
            <p><a href="mailto:contact@wildrescues.net">contact@wildrescues.net</a></p>
        </footer>

    </body>
</html>'''

with open('rescue/index.html', 'w') as f:
    f.write(index_html)
print('Updated index.html')

# Tasks 10, 11, 12: Create about.html
about_html = '''<!-- Write your code here --><!DOCTYPE html>
<!--
    Student Name: Mike Dahlin
    File Name: about.html
    Date: 06/24/2026
-->
<html lang="en">
    <head>
        <title>Wild Rescues: About Us</title>
        <meta charset="utf-8">
    </head>
    <body>

        <header>
            <h1>&#128062; Wild Rescues</h1>
            <h3>Rescue. Rehabilitate. Release.</h3>
        </header>

        <nav>
            <p><a href="index.html">Home</a> &nbsp; &#9672; &nbsp;
<a href="about.html">About Us</a> &nbsp; &#9672; &nbsp;
<a href="partnership.html">Partnership</a> &nbsp; &#9672; &nbsp;
<a href="gallery.html">Gallery</a> &nbsp; &#9672; &nbsp;
<a href="faqs.html">FAQs</a> &nbsp; &#9672; &nbsp;
<a href="contact.html">Contact</a></p>
        </nav>

        <main>
            <div id="info">
                <h2>About Us</h2>
                <p>Wild Rescues is a registered nonprofit wildlife rescue and rehabilitation facility, located in Ocala, Florida. We help injured, sick, neglected, and orphaned wildlife. We help rehabilitate these animals and then release them back into the wild, if possible.</p>

                <p>Wild Rescues is a member of the <a href="https://www.nwrawildlife.org/" target="_blank">National Wildlife Rehabilitators Association</a>.</p>


                <img src="images/tortoise.jpg" alt="tortoise eating vegetation" height="300" width="400">


                <h3>We help many animals, such as:</h3>
                <ul>
                    <li>Raccoons</li>
                    <li>Squirrels</li>
                    <li>Fox</li>
                    <li>Birds</li>
                    <li>Horses</li>
                    <li>Deer</li>
                    <li>Pigs</li>
                    <li>Reptiles</li>
                </ul>


                <p>Did you find an injured or orphaned animal? Contact us to see if we can help.</p>
            </div>
        </main>

        <footer>
            <p>&copy; Copyright 2021. All Rights Reserved.</p>
            <p><a href="mailto:contact@wildrescues.net">contact@wildrescues.net</a></p>
        </footer>

    </body>
</html>'''

with open('rescue/about.html', 'w') as f:
    f.write(about_html)
print('Created about.html')

# Tasks 13, 14, 15, 16: Create contact.html
contact_html = '''<!-- Write your code here --><!DOCTYPE html>
<!--
    Student Name: Mike Dahlin
    File Name: contact.html
    Date: 06/24/2026
-->
<html lang="en">
    <head>
        <title>Wild Rescues: Contact</title>
        <meta charset="utf-8">
    </head>
    <body>

        <header>
            <h1>&#128062; Wild Rescues</h1>
            <h3>Rescue. Rehabilitate. Release.</h3>
        </header>

        <nav>
            <p><a href="index.html">Home</a> &nbsp; &#9672; &nbsp;
<a href="about.html">About Us</a> &nbsp; &#9672; &nbsp;
<a href="partnership.html">Partnership</a> &nbsp; &#9672; &nbsp;
<a href="gallery.html">Gallery</a> &nbsp; &#9672; &nbsp;
<a href="faqs.html">FAQs</a> &nbsp; &#9672; &nbsp;
<a href="contact.html">Contact</a></p>
        </nav>

        <main>
            <div id="contact">
                <h2>You can reach us at:</h2>
                <p>Office: (814) 555-8989</p>
                <p>Email: <a href="mailto:contact@wildrescues.net">contact@wildrescues.net</a></p>
                <p>Address: <a href="https://goo.gl/maps/BTJzjc2tALd4RDWA8" target="_blank">8989 Rescue Drive, Ocala, FL 34471</a></p>
            </div>
        </main>

        <footer>
            <p>&copy; Copyright 2021. All Rights Reserved.</p>
            <p><a href="mailto:contact@wildrescues.net">contact@wildrescues.net</a></p>
        </footer>

    </body>
</html>'''

with open('rescue/contact.html', 'w') as f:
    f.write(contact_html)
print('Created contact.html')

print('All tasks completed!')
