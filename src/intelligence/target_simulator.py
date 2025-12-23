"""
ARES Target Simulator
Generates high-fidelity mock target data for testing AI and coordination.
"""
import random
import time

class TargetSimulator:
    def __init__(self, area_center=(39.9334, 32.8597)): # Default: Ankara
        self.center = area_center
        self.target_types = ["ARMORED", "INFANTRY", "UAV", "RADAR"]

    def generate_random_target(self, id_prefix="TARGET"):
        """Generates a random target within a 5km radius."""
        target_id = f"{id_prefix}-{random.randint(100, 999)}"
        target_type = random.choice(self.target_types)
        
        # Simple coordinate jitter
        lat = self.center[0] + (random.random() - 0.5) / 10
        lon = self.center[1] + (random.random() - 0.5) / 10
        
        threat_level = round(random.uniform(0.1, 1.0), 2)
        
        return {
            "id": target_id,
            "type": target_type,
            "coords": (lat, lon),
            "threat": threat_level,
            "timestamp": time.time()
        }

if __name__ == "__main__":
    sim = TargetSimulator()
    while True:
        target = sim.generate_random_target()
        print(f"[SIM] Target Spotted: {target['type']} at {target['coords']} (Threat: {target['threat']})")
        time.sleep(3)
