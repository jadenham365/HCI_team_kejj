extends KinematicBody2D
const UP = Vector2(0,-1)
const MAXSPEED = 120
const MAXFALLSPEED = 300
const SPRINTBOOST = 2
const GRAVITY = 600
const JUMPPOWER = 200
var coins = 0
var motion = Vector2()
signal win
var failed_grabs = 0


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	# Left and right movements
	
	if Input.is_action_pressed("right") and not Input.is_action_pressed("left"):
		if Input.is_action_pressed("sprint"):
			motion.x = MAXSPEED * SPRINTBOOST
		else:
			motion.x = MAXSPEED
	elif Input.is_action_pressed("left") and not Input.is_action_pressed("right"):
		if Input.is_action_pressed("sprint"):
			motion.x = -MAXSPEED * SPRINTBOOST
		else:
			motion.x = -MAXSPEED
	else:
		motion.x = 0
		
	
#	if Input.is_action_pressed("up") and not Input.is_action_pressed("down"):
#		motion.y = -MAXSPEED
#	elif Input.is_action_pressed("down") and not Input.is_action_pressed("up"):
#		motion.y = MAXSPEED
#	else:
#		motion.y = 0

	motion.y += GRAVITY * delta
	if motion.y > MAXFALLSPEED:
		motion.y = MAXFALLSPEED

	if Input.is_action_pressed("jump") and is_on_floor():
		motion.y = -JUMPPOWER
	
	motion = move_and_slide(motion,UP)

func _on_door_body_entered(body):
	if get_tree().get_nodes_in_group("coin_group").size() == 0: 
		get_tree().reload_current_scene()
		emit_signal("win")

# TODO: add 1 to coins
# if we have a winning number of coins, emit signal "win" and make yourself invisible
func _on_coin_body_entered(body):
	if Input.is_action_pressed("grab"):
		coins += 1
		#queue_free()
		#print(coins)
		
func _on_coin_body_exited(body):
	pass
