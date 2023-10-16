extends RichTextLabel

var time = 0
var show_time = false
var win_time = "0"


# Called when the node enters the scene tree for the first time.
func _ready():
	var playernode = get_tree().get_root().find_node("Player", true, false)
	playernode.connect("win", self, "handlewin")
	# TODO: make invisible on start
	
func handlewin():
	show_time = true

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if show_time:
		# TODO: show a winning screen with the player's time
		pass
	else:
		time += delta
	
