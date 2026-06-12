<!--practice-->

You have already created a responsive design website for a dog grooming business, but now need to add a video to the website and make it accessible.

## Perform the following tasks:

1. Open your _groom_ folder and create a new subfolder named **media**. Move the provided media files from the _resources_ folder into your _groom/media_ folder by either drag and drop or copy and paste.

2. Open the _index.html_ file and add a `video` element at the end of the `welcome` `div`. Include the controls attribute and a poster attribute that uses the image file of your choice.

3. Nest a `source` element within the `video` element that specifies _groom.mp4_ as the source file and **video/mp4** as the `type`.

4. Nest another `source` element that specifies _groom.webm_ as the source file and **video/webm** as the `type`.

5. Open the _media\captions.vtt_ file and add your name and date to the **NOTE**. Use _Table 9-9_ to create a captions file:

<p align='center'>
<img src='../assets/ROvgCI7wRJu3lEmhrU5l.png' width='95%' alt='Table with 19 rows and 2 columns. The column headings from left to right are Line Number and Code to Insert. The row details are as follows. Row 1: Line Number, 9; Code to Insert, 1. Row 2: Line Number, 10; Code to Insert, 0 0 colon 0  5 period 0 0 0 dash dash bracket 0 0 colon 0 9 period 4 0 0. Row 3: Line Number, 11; Code to Insert, All of our grooming packages include a relaxing bath.  Row 4: Line Number, 12; Code to Insert, empty cell. Row 5: Line Number, 13; Code to Insert, 2. Row 6: Line Number, 14; Code to Insert, 0 0 colon 1 2 period 3 0 0 dash dash bracket 0 0 colon 1 4 period 7 0 0. Row 7: Line Number, 15; Code to Insert, Nails are carefully trimmed. Row 8: Line Number, 16; Code to Insert, empty cell. Row 9: Line Number, 17; Code to Insert, 3. Row 10: Line Number, 18; Code to Insert, 0 0 colon 1 6 period 7 0 0 dash dash bracket 0 0 colon 1 9 period 9 0 0. Row 11: Line Number, 19; Code to Insert, Our groomers cut and style with precision. Row 12: Line Number, 20; Code to Insert, empty cell. Row 13: Line Number, 21; Code to Insert, 4. Row 14: Line Number, 22; Code to Insert, 0 0 colon 2 3 period 6 0 0 dash dash bracket 0 0 colon 2 6 period 3 0 0. Row 15: Line Number, 23; Code to Insert, We offer several grooming packages. Row 16: Line Number, 24; Code to Insert, empty cell. Row 17: Line Number, 25; Code to Insert, 5. Row 18: Line Number, 26; Code to Insert, 0 0 colon 2 8 period 0 0 0 dash dash bracket 0 0 colon 3 2 period 0 0 0. Row 19: Line Number, 27; Code to Insert, Let us pamper your pet today.' />
</p>
<sup>Table 9-9</sup>

6. Use the `track` element to add the captions file to the `video` element. Include the following attributes: `src`, `kind`, `srclang`, and `label`.

7. Use the `track` element to add the descriptions file to the `video` element. Include the following attributes: `src`, `kind`, `srclang`, and `label`.

8. Below the `source` element, provide fallback text for legacy browsers that do not support the `video` element.

9. Open the _styles.css_ file in your text editor. Add the `video` selector to the CSS Reset style rule. Add the `video` selector to the `img` style rule as well.

10. Launch the website in a new tab and use Web Server for Chrome to launch the website. Turn the captions on and view the video with captions.

11. Check your spelling. Validate all HTML and CSS files and correct any errors.

> Identify the steps you would take to accommodate legacy browsers if you included a Flash video on the Dog Grooming website.

<!--
{
    "CopyExercise": {
        "name": "Chapter 8 YT02",
        "copyTarget": "/chapter8/yt02/student/*",
        "pasteTarget": "./"
    }
}
-->
