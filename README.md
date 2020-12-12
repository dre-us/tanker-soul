# tanker-soul

This is a battle tank game where you have a lot of worlds to play.<br>
to try this game you must download the folder and run main.py (you should have installed pygame)

## worlds
One world is modeling by a vector of positions, where each component is the height of the ground, changing the vector will change the world.
The floor was built using the linear equation of a straight applied to adjacents points in the world vector.

## tank
Each tank has its own velocity, health and its own (and maybe) unique way of shotting.
shotting can be doing with diferents angles.

## projectile
It was implemented with the equation of projectile motion.
Each projectile has a certain amount of damage when this impacts another tank.

## movements

<p>rigth arrow -> move to the rigth</p>
<p>left arrow -> move to the left</p>
<p>up arrow -> increase the angle of the cannon tank</p>
<p>down arrow -> decrease the angle of the cannon tank</p>
<p>space -> shot</p>

## screenshots
<img src="images/moving.gif"
alt="tank moving"
style="float: left; margin-right: 10px;"
width="200px"/>
<img src="images/one_shot.gif"
alt="one shot of a tank"
style="float: left; margin-right: 10px;"
width="200px"/>
<img src="images/many_shots.gif"
alt="many shots of one tank"
style="float: left; margin-right: 10px;"
width="200px"/>
<br><br>
<img src="images/shotting_and_moving.gif"
alt="tank moving and shotting"
style="float: left; margin-right: 10px;"
width="200px"/>
<img src="images/shotting_up_and_moving.gif"
alt="tank shotting upwars and moving"
style="float: left; margin-right: 10px;"
width="200px"/>
