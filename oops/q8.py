class camera:
    def take_photo(self):
        print("Photo captured using camera")
    
    def record_video(self):
        print("Video recorded using camera")
    
class phone:
    def make_call(self, number):
        print(f"Calling {number}....")

    def send_message(self,message):
        print(f"Sending message to {message}....")

class SmartPhone(camera,phone):
    def browse_internet(self):
        print("Browsing the internet using smartphone")


sp = SmartPhone()

sp.take_photo()
sp.record_video()
sp.make_call("1234567890")
sp.send_message("Hello, how are you?")
sp.browse_internet()
