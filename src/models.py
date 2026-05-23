class Meal:
    """Represents a meal with nutritional and dietary information."""
    
    def __init__(self, id, name, health_score, keto_potential, gf_potential):
        """
        Initialize a Meal object.
        
        Args:
            id: Unique identifier for the meal
            name: Name of the meal
            health_score: Health score rating (0-100)
            keto_potential: Whether meal is keto-friendly (True/False)
            gf_potential: Whether meal is gluten-free (True/False)
        """
        self.id = id
        self.name = name
        self.health_score = health_score
        self.keto_potential = keto_potential
        self.gf_potential = gf_potential
    
    # Getters
    def get_id(self):
        """Return the meal ID."""
        return self.id
    
    def get_name(self):
        """Return the meal name."""
        return self.name

    def get_health_score(self):
        """Return the health score."""
        return self.health_score
    
    def get_keto_potential(self):
        """Return the keto potential."""
        return self.keto_potential

    def get_gf_potential(self):
        """Return the gluten-free potential."""
        return self.gf_potential

    # Setters
    def set_name(self, name):
        """Set the meal name."""
        self.name = name
    
    def set_health_score(self, health_score):
        """Set the health score."""
        self.health_score = health_score
    
    def set_keto_potential(self, keto_potential):
        """Set the keto potential."""
        self.keto_potential = keto_potential
    
    def set_gf_potential(self, gf_potential):
        """Set the gluten-free potential."""
        self.gf_potential = gf_potential
    
    # Utility methods
    def to_dict(self):
        """Convert meal object to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'healthScore': self.health_score,
            'ketoPotential': self.keto_potential,
            'gfPotential': self.gf_potential
        }
    
    def __repr__(self):
        """Return string representation of the meal."""
        return f"Meal(id={self.id}, name='{self.name}', health_score={self.health_score}, keto={self.keto_potential}, gf={self.gf_potential})"
    
    def __str__(self):
        """Return human-readable string of the meal."""
        return f"{self.name} (Health: {self.health_score}, Keto: {self.keto_potential}, GF: {self.gf_potential})" 