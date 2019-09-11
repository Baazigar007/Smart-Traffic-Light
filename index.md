
<h2 align="center">What is the Problem ??</h2>


    With increasing urban population and hence the number of vehicles, 
    need of controlling streets,highways and roads is major issue. 
    
One of the main reasons behind today’s traffic problem are the techniques that are used for traffic
management. It has no emphasis on _live traffic scenario_, thus leading to inefficient traffic management systems.
These traffic timers just show the preset time.
    
If the traffic light timers are showing correct time to regulate the traffic, then the time wasted on unwanted green
    signals will be saved. Timer for every lane is the simplest way to control traffic. 
    And if those timers are predicting exact time then automatically the system will be more efficient.
    
<img src="https://www.transportation.gov/sites/dot.gov/files/2.jpg" width="1000" height="500">
    
*** 

<h2 align="center">How is it Solved ??</h2>
    
    The most appropriate solution to the Congestion problem is letting the congested sides cross the intersection first.
    
The above proposed solution can be implemented using **OpenCv** library in Python or **Machine Learning** via 
    Object Detection to count the number of cars in an image and also differentiate between the different types of vehicles.
    
<h3 align="center">OpenCv Approach </h3>

Placing a Camera on each side of the intersection and Processing the images to get the number of vehicles 
    on each side of the intersection .
    
    The Image taken is processed :
    1. Read using OpenCv Library in Python
    2. resized according to need
    3. Converted to Black and White 
    4. Removing Gaussian Noise
    5. Removing Salt and Pepper Noise 
    6. Dilation
    7. Take Difference from reference image 
    8. Find the percentage change 
    9. Get Number of Cars

<h3 align="center">Black and White Image  </h3>

![Image](/IMG/Proc1.jpg)

<h3 align="center">Edge Detection Image</h3>

![Image](/IMG/Proc2.jpg)

<h3 align="center">Machine Learning Approach </h3>
    
Capturing an image of each side of the intersection and passing it to the object detection module to get the 
    number of different vehicles on different sides of the intersection.
    
    The Image taken is :
    1. Preprocessed to determine its path
    2. Either a Model is inherited or New one is made to detect cars and different vehicles
    3. Image is loaded and all the detections are saved and lated analysed 
    4. Cars are counted in the Detections 
    
 
<h3 align="center">Input Image</h3> 

![Image](/IMG/image.jpg)

<h3 align="center">Detected Objects</h3>

![Image](/IMG/imagenew.jpg)

***

<h2 align="center">How are these Numbers manipulated ??</h2>

Once stored in a list the number of cars are manipulated to clear the congestion as soon as possible .
    
Considering a single car's contribution in a 3 lane road is of 2 seconds to cross the intersection ,
if the value of the number of cars dont exceed 10 ( Normal Value ) then the normal clockwise flow of the 
traffic is maintained else the congested traffic algorithm comes in play and handles the situation .
    
```python
if List[MaxIndex]<=NormVal :
    NormalTrafficS(List)
else :
    CongestedTrafficS(List)
```

<h4 align="center">Conditions </h4>

- [x] __Cycle is completed__ i.e Once a signal is green , it turns green again once all 3 other signals get there chance .

- [x] __Max Waiting time__ i.e The maximum waiting time for any side is 180 seconds or 3 minutes.

- [x] __Few Car case__ i.e If a side has  very less number of cars for eg. 3 then the corresponding side will turn to green instead of making those few cars wait for 180 seconds at max .
    
- [x] __Single sided case__ i.e In a situation there is just one sided traffic flow and all the other sides of the intersection are empty then complete preference will be given to the corresponding side.**This is very useful in situations like evacuation**
    
    
<h3 align="center">Types of Congested traffic clearing algorithms  </h3>

    Two types of algorithms are developed in the project :
    1. Variance-Based Algorithm
    2. Slab Division Algorithm 

<h4 align="center">Variance-Based Algorithm  </h4>

    The variance in probability theory and statistics is a way to measure how far a set of numbers is spread out. 
    Variance describes how much a random variable differs from its expected value. The variance is defined 
    as the average of the squares of the differences between the individual (observed) and the expected value.
    
```python
VarianceVal=Variance(List)
    if VarianceVal<100:
        return 25
    elif VarianceVal<200:
        return 40
    elif VarianceVal<400:
        return 50
    else:           #maximum 650 
        return 60
```
    
Once Variance of the Number of the cars on the 4 sides is calculated , the program will know how spread out the numbers are and will alot the Time for Green light on each side depending upon the value of variance .
Timers according to variance are used to make the data less spread out and it also tends to bring the maximum value close and in cases even less than second and third maximum number in the list thus making the List less complex and maintaining uniformity.
Use of Variance for alloting the time for Green signal improves the efficiency as the algorithm becomes more dynamic and situation dependent instead of being static .

For eg: 
-  List = [40,50,45,43] 
    - Will result in Low variance (13.25) and thus providing similar and comparitively less time for each side Green signal will be fair and performance wise relevant.

- List = [1,2,4,60]
    - Will result in High variance (624.6) and after taking in consideration the _Few Car Case_ performance wise relevant timimgs will be alloted 

- List = [5,20,30,45]
    - Will result in Moderate variance (212.5) and a timer of maximum 50 seconds will be alloted 
    
<h4 align="center">Slab Division Algorithm </h4> 

    Slab consists of set of numbers with a lower and upper bound. Making slabs and dividing the number of cars 
    on the basis of slabs and alloting appropriate time can be done to make the congested traffic flow more smoothly.
    
```python
'''
SLABS
Congestion_0 - 00-10  -->20 secs
Congestion_1 - 10-40  -->40 secs
Congestion_2 - 40-60  -->60 secs
'''
```

Once the number of cars on each side of the intersection is calculated , Slabs can be used to alot timimgs to different sides with the side with maximum number of cars given the priority of crossing the intersection and taking care of the above conditions so as to keep the flow of traffic efficient , smooth and fair .
Timers to the slabs are alloted so as to make the maximum number of cars in that slab half , by letting half of the cars pass the intersection , Considering the contribution of a single car in a three lane road is 2 second . 

For eg: 
- List = [10,20,30,40] 
    - Contains three elements of slab _1_ and one of slab _2_ initially and will later change according to the values 
    
Variance-Based Algorithm | Slabs-Division Algorithm
------------------------ | ------------------------
Calculates the Time according to the variance of the List | Calculates the Time according to the Value of a single Index
Results in a more Dynamic approach | Comparitively lesser Dynamic then Variance-Based 
More Efficient | Comparitively lesser Efficient 

***

<h2 align="center">Output Examples  </h2>

<h3 align="center">Normal Version Output </h3>

![Image](/IMG/Op.png)

<h3 align="center">Prototype Extended Version Output </h3>

![Image](/IMG/Proto.png)

***

<h2 align="center">Constraints  </h2>

- At Max 60 cars can be accomodated in the camera frame 
- Getting Image of an empty road for reference image 
- Object detection sometimes detects same vehicle as both car and truck simultaneously
- Image Noise 

***

<h2 align="center">Future Scope </h2>

- Can be developed for three lanes of each side of the road ( Prototype Extended Version )
- Can be moulded to be used in situations like mass evacuation 
- Linking of other traffic lights in sync to provide better congestion clearing 
- Can be developed further to be used by emergency vehicles to provide Green route and decreasing accidents on intersections.

***

<h2 align="center">Wanna Help ?? Contact Me :</h2>
 
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.linkedin.com/in/vaibhav-sethia-4711b8145/" rel="some text"  >![Foo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4gb4hSdBab5OaZmXU36ujdk9MtdpDF-nV55T0du5pMvEtDr4m)</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://mail.google.com/mail/u/0/#inbox?compose=DmwnWrRvwLzWfFqlwLLWnvHtFhWCPpWWhgMTnFMGJdmgWRpnXsTRLkTLzjDjHWqVkLZQQRLWrfZQ" rel="some text" align="center" >![Foo](https://cdn2.iconfinder.com/data/icons/social-icons-color/512/gmail-128.png)</a>
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/vaibhavsethia" rel="some text" align="center" >![Foo](https://www.freeicons.io/laravel/public/uploads/icons/png/13855371531555590081-128.png)</a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 <a href="https://www.instagram.com/vaibhav_9_8/" rel="some text" align="right" >![Foo](https://turningheadsfi.files.wordpress.com/2018/08/instagram-logo-128x128.png)</a>


