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
	var secs = fmod(time, 60)
	var mins = fmod(time, 3600) / 60
	var millis = int((secs - int(secs)) * 1000)
	win_time = "%02d:%02d.%03d" % [mins, secs, millis]
	print("Time: " + win_time)
	time = 0
	

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	time += delta
	
