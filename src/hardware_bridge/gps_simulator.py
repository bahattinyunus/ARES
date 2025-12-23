"""
ARES GPS Simulator
Simulates tactical positioning and GPS-Denied scenarios.
"""
import random
import time

class GPSSimulator:
    def __init__(self, initial_pos=(39.9334, 32.8597)):
        self.current_pos = initial_pos
        self.jamming_active = False

    def get_position(self):
        """Returns the current GPS position, or None if jammed."""
        if self.jamming_active:
            print("[WARN] GPS Signal Jammed (Electronic Warfare Active)")
            return None
        
        # Add slight movement drift
        lat = self.current_pos[0] + (random.random() - 0.5) / 1000
        lon = self.current_pos[1] + (random.random() - 0.5) / 1000
        self.current_pos = (lat, lon)
        
        return self.current_pos

    def toggle_jamming(self):
        """Toggles the simulated Electronic Warfare state."""
        self.jamming_active = not self.jamming_active
        status = "ENABLED" if self.jamming_active else "DISABLED"
        print(f"[*] Electronic Warfare Jamming: {status}")
