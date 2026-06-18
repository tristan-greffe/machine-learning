from pathlib import Path

# Root directory for all dataset outputs (model/dataset/)
DATASET_DIR = Path(__file__).parent

# NOTE: data.geopf.fr (IGN WMTS) covers France metropolitan + overseas territories only.
# Other European countries require a different tile source.

# Training zones for buildings: name → (latitude, longitude, grid_tiles)
BUILDING_ZONES = {
    # Dense urban — France metropolitan
    "paris_centre":         (48.8566,  2.3522,  8),
    "paris_marais":         (48.8580,  2.3620,  8),
    "lyon_presquile":       (45.7600,  4.8350,  8),
    "marseille_centre":     (43.2950,  5.3700,  8),
    "bordeaux_centre":      (44.8378, -0.5792,  8),
    "toulouse_centre":      (43.6047,  1.4442,  8),
    "lille_centre":         (50.6292,  3.0573,  8),
    "nantes_centre":        (47.2184, -1.5536,  8),
    "montpellier_centre":   (43.6110,  3.8770,  8),
    "nice_centre":          (43.7000,  7.2700,  8),
    "strasbourg_centre":    (48.5734,  7.7521,  8),
    "rennes_centre":        (48.1173, -1.6778,  8),
    "grenoble_centre":      (45.1885,  5.7245,  8),
    "dijon_centre":         (47.3220,  5.0415,  8),
    "clermont_centre":      (45.7772,  3.0870,  8),
    # Suburban / residential
    "periurbain_yvelines":  (48.7600,  1.9500,  8),
    "periurbain_essonne":   (48.6500,  2.4500,  8),
    "periurbain_lyon":      (45.7000,  4.9500,  8),
    "lotissement_moderne":  (48.9100,  2.0500,  8),
    # Villages
    "village_alsace":       (48.0720,  7.3580,  6),
    "village_bretagne":     (47.8900, -3.0050,  6),
    "village_provence":     (43.7200,  5.4000,  6),
    "village_normandie":    (49.1000,  0.1500,  6),
    # Industrial / commercial
    "zone_industrielle":    (48.8200,  2.4500,  8),
    "zone_commerciale":     (48.8400,  2.5400,  8),
    # French overseas territories (DOM-TOM)
    "fort_de_france":       (14.6037, -61.0710,  8),  # Martinique
    "saint_denis_reunion":  (-20.8823, 55.4504,  8),  # Réunion
    "cayenne":              ( 4.9224, -52.3135,  8),  # Guyane
    "pointe_a_pitre":       (16.2415, -61.5331,  8),  # Guadeloupe
}

# Training zones for pools: name → (latitude, longitude, half_extent_deg)
# half_extent_deg defines the Overpass query bounding box: ±half around center
POOL_ZONES = {
    # Côte d'Azur — highest pool density in France
    "antibes":              (43.5830,  7.1100,  0.04),
    "cannes":               (43.5600,  7.0200,  0.04),
    "mougins":              (43.6000,  7.0000,  0.04),
    "saint_tropez":         (43.2677,  6.6400,  0.04),
    "frejus":               (43.4330,  6.7370,  0.04),
    "nice_ouest":           (43.6800,  7.1800,  0.04),
    # Provence / Languedoc
    "aix_en_provence":      (43.5300,  5.4400,  0.04),
    "marseille_sud":        (43.2400,  5.4200,  0.04),
    "toulon":               (43.1400,  5.9300,  0.04),
    "montpellier":          (43.6300,  3.8500,  0.04),
    "perpignan":            (42.6900,  2.9000,  0.04),
    "nimes":                (43.8200,  4.3600,  0.04),
    "avignon":              (43.9300,  4.8000,  0.04),
    # South-West
    "toulouse_ouest":       (43.5900,  1.3500,  0.04),
    "bordeaux_sud":         (44.7400, -0.6200,  0.04),
    "arcachon":             (44.6600, -1.1700,  0.04),
    # Île-de-France residential suburbs
    "idf_yvelines":         (48.7700,  1.9200,  0.04),
    "idf_seine_et_marne":   (48.6200,  2.7500,  0.04),
    "lyon_ouest":           (45.7800,  4.7500,  0.04),
    # French overseas — tropical areas with high pool density
    "martinique_nord":      (14.7200, -61.0500,  0.04),
    "reunion_ouest":        (-21.0500,  55.2300,  0.04),
    "guadeloupe_basse":     (16.1800, -61.7200,  0.04),
}
