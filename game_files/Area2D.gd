extends Area2D


# Called when the node enters the scene tree for the first time.
func _ready():
	var playernode = get_tree().get_root().find_node("Player", true, false)
	playernode.connect("win", self, "handlewin")


# TODO: Make the coins invisible on a win
func handlewin():
	pass


# TODO: Delete the coin when it is entered by another body
func _on_coin_body_entered(body):
	pass
