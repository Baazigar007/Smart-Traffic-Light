# Smart-Traffic-Light

## What is the Problem ??

    With increasing urban population and hence the number of vehicles, need of controlling streets, highways and roads is
    major issue. 
One of the main reasons behind today’s traffic problem are the techniques that are used for traffic
management. It has no emphasis on live traffic scenario, thus leading to inefficient traffic management systems.
These traffic timers just show the preset time.
    
If the traffic light timers are showing correct time to regulate the traffic, then the time wasted on unwanted green
    signals will be saved. Timer for every lane is the simplest way to control traffic. 
    And if those timers are predicting exact time then automatically the system will be more efficient.
    
![Image](https://www.transportation.gov/sites/dot.gov/files/2.jpg)


## How is it [Solved](https://webchronicletoday.com/2019/09/05/intelligent-traffic-management-system-market-ability-to-improve-efficiency-in-various-situations-including-mobility-and-road-transport-to-boost-the-market/) ??
    
    The most appropriate solution to the Congestion problem is letting the congested sides cross the intersection first.
    
The above proposed solution can be implemented using **OpenCv** library in Python or **Machine Learning** via 
    Object Detection to count the number of cars in an image and also differentiate between the different types of vehicles.
    
### OpenCv Approach 

Placing a Camera on each side of the intersection and Processing the images to get the number of vehicles 
    on each side of the intersection .
    
    The Image taken is processed :
    - [x] Read using OpenCv Library in Python
    2. resized according to need
    3. Converted to Black and White 
    4. Removing Gaussian Noise
    5. Removing Salt and Pepper Noise 
    6. Dilation
    7. Take Difference from reference image 
    8. Find the percentage change 
    9. Get Number of Cars


#### Black and White Image 
<img src="/IMG/image-1 copy.jpg" alt="Image BW"/>

#### Edge Detection Image
<img src="/IMG/image copy.jpg" alt="Edge Detection"/>


### Machine Learning Approach 
    
Capturing an image of each side of the intersection and passing it to the object detection module to get the 
    number of different vehicles on different sides of the intersection.
    
    The Image taken is :
    1. Preprocessed to determine its path
    2. Either a Model is inherited or New one is made to detect cars and different vehicles
    3. Image is loaded and all the detections are saved and lated analysed 
    4. Cars are counted in the Detections 
    
 
#### Input Image  
<img src="/IMG/image.jpg" alt="Input"/>

#### Detected Objects
<img src="/IMG/imagenew.jpg" alt="Output"/>
  

```python

```
## How are these Numbers manipulated ??

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

#### Conditions :

- [x] __Cycle is completed__ i.e Once a signal is green , it turns green again once all 3 other signals get there chance .

- [x] __Max Waiting time__ i.e The maximum waiting time for any side is 180 seconds or 3 minutes.

- [x] __Few Car case__ i.e If a side has very less number of cars eg. 3 then the corresponding side will turn to green instead of making those few cars wait for 180 seconds at max .
    
- [x] __Single sided case__ i.e In a situation there is just one sided traffic flow and all the other sides of the intersection are empty then complete preference will be given to the corresponding side.**This is very useful in situations like evacuation**
    
    
### Types of Congested traffic clearing algorithms 

    Two types of algorithms are developed in the project :
    1. Variance-Based Algorithm
    2. Slab Division Algorithm 

#### Variance-Based Algorithm 

#### Slab Division Algorithm 

## Constraints & Future Scope 



