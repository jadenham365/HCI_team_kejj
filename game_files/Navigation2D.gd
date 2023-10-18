extends Navigation2D


# Called when the node enters the scene tree for the first time.
func _ready():
	var playernode = get_tree().get_root().find_node("Player", true, false)
	playernode.connect("win", self, "handlewin")


# TODO: make map invisible when a player wins
func handlewin():
	pass


func _on_coin_body_exited(body):
	pass # Replace with function body.
