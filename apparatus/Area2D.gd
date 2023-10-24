# Global.gd
extends Area2D

var is_player_inside = false
var missed_s = 0
# Called when the node enters the scene tree for the first time.
func _ready():
	pass
# restart game once player enters door
func _on_door_body_entered(body):
	pass
		#get_tree().reload_current_scene()


func _process(delta):
	if is_player_inside and Input.is_action_just_pressed("grab"):
		queue_free()
	if not is_player_inside and Input.is_action_just_pressed("grab"):
		missed_s += 1
	Global.missed = missed_s
	
	
# TODO: Delete the coin when it is entered by another body

func _on_coin_body_entered(body):
	is_player_inside = true
		#print(get_tree().get_nodes_in_group("coin_group").size())

func _on_coin_body_exited(body):
	is_player_inside = false

