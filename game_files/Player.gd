extends KinematicBody2D
const UP = Vector2(0,-1)
const MAXSPEED = 120
var coins = 0
var motion = Vector2()
signal win


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	# Left and right movements
	if Input.is_action_pressed("right") and not Input.is_action_pressed("left"):
		motion.x = MAXSPEED
	elif Input.is_action_pressed("left") and not Input.is_action_pressed("right"):
		motion.x = -MAXSPEED
	else:
		motion.x = 0
		
	if Input.is_action_pressed("up") and not Input.is_action_pressed("down"):
		motion.y = -MAXSPEED
	elif Input.is_action_pressed("down") and not Input.is_action_pressed("up"):
		motion.y = MAXSPEED
	else:
		motion.y = 0
	
	motion = move_and_slide(motion,UP)


# TODO: add 1 to coins
# if we have a winning number of coins, emit signal "win" and make yourself invisible
func _on_coin_body_entered(body):
	pass

