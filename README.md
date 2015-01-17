# major-breadth-overlaps
Looks through UC Berkeley webpages to see which classes required for majors/minors can also be 
used to fulfill breadth requirements.


<h2>majorBreadthOverlaps.py</h2>
Upon running <code>python majorBreadthOverlaps.py</code> with majors Computer Science and Physics, and minor Spanish Linguistics, 
you will see:
    
    Enter the following with semicolons (;) separating multiple majors/minors. 
    What majors are you considering? Computer Science; Physics
    What minors are you considering? Spanish Linguistics
    
    Spanish Linguistics
    ------------------------------------------------
    Spanish 3: International Studies
    Spanish 4: International Studies
    Spanish 25: Arts & Literature
    Spanish 100: Social and Behavioral Sciences
    Spanish 161: Social and Behavioral Sciences
    Spanish 162: Social and Behavioral Sciences
    Spanish 179: Social and Behavioral Sciences
    
    Physics
    ------------------------------------------------
    Physics 177: Biological Sciences
    
    Computer Science
    ------------------------------------------------
    Psychology 101: Social and Behavioral Sciences
    Geography 143: Physical Science, Biological Sciences
    Earth and Planetary Science 104: Physical Science
    Architecture 122: Social and Behavioral Sciences
    Computer Science 61C: Physical Science
    Computer Science 188: Physical Science
    Computer Science 61C: Physical Science



<h2>deptBreadths.py</h2>
You can also run <code>python deptBreadths.py</code> to list all courses in a given department that fulfill breadths. 
Upon running this with the Computer Science and Mathematics departments, you will see:

    
    Enter the departments for which you want to list all L&S breadth classes, separated by semicolons: Computer Science; Mathematics
    
    Mathematics
    ==========================================================================
    103: Social and Behavioral Sciences
    125A: Philosophy & Values
    125B: Philosophy & Values
    135: Philosophy & Values
    160: Historical Studies
    
    Computer Science
    ==========================================================================
    188: Physical Science
    39B: Historical Studies
    39C: Historical Studies
    39D: Philosophy & Values
    39E: Historical Studies
    39F: Physical Science
    39K: Historical Studies
    39M: Social and Behavioral Sciences, Philosophy & Values
    61C: Physical Science
    61CL: Physical Science
    C182: Social and Behavioral Sciences, Biological Sciences

