extends RichTextLabel

var time = 0
var show_time = false
var win_time = "0"
# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	var playernode = get_tree().get_root().find_node("Player", true, false)
	playernode.connect("win", self, "handlewin")
	print("done")
	self.visible = true
	
func handlewin():
	show_time = true
	print("signialed")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	set_text("You Win!")
	newline()
	add_text("Time:")
	time += delta
	if show_time:
		self.visible = true
		var secs = fmod(time,60)
		var mins = fmod(time,60*60)/60
		win_time = "%02d : %02d" % [mins,secs]
		newline()
		add_text(win_time)
		
