extends Area2D


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

# TODO: Delete the coin when it is entered by another body
func _on_coin_body_entered(body):
	if Input.is_action_pressed("ui_accept"):
		self.queue_free()
		#print(get_tree().get_nodes_in_group("coin_group").size())
