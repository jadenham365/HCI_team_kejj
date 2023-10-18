extends Area2D

var is_player_inside = false

# Called when the node enters the scene tree for the first time.
func _ready():
	var playernode = get_tree().get_root().find_node("Player", true, false)
	playernode.connect("win", self, "handlewin")


# TODO: Make the coins invisible on a win
func handlewin():
	pass

# restart game once player enters door
func _on_door_body_entered(body):
	pass
		#get_tree().reload_current_scene()


func _process(delta):
	if is_player_inside and Input.is_action_just_pressed("grab"):
		queue_free()
# TODO: Delete the coin when it is entered by another body

func _on_coin_body_entered(body):
	is_player_inside = true
		#print(get_tree().get_nodes_in_group("coin_group").size())

func _on_coin_body_exited(body):
	is_player_inside = false

