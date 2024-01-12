# Conversion factors
CM_PER_M = 100
MM_PER_CM = 10
NS_PER_S = 1e9

# Slope of the line of best fit for DSPS angle
CM_PER_RAD = 34.14230382

# y-limit of each DSPS
Y_LIM = 10 * MM_PER_CM

# Detector dimensions
DETECTOR_SIZE_X_M = 1.78
DETECTOR_SIZE_Y_M = 1.78
DETECTOR_SIZE_Z_M = 1.78
DETECTOR_SIZE_M = (DETECTOR_SIZE_X_M, DETECTOR_SIZE_Y_M, DETECTOR_SIZE_Z_M)

DETECTOR_SIZE_X_CM = DETECTOR_SIZE_X_M * CM_PER_M
DETECTOR_SIZE_Y_CM = DETECTOR_SIZE_Y_M * CM_PER_M
DETECTOR_SIZE_Z_CM = DETECTOR_SIZE_Z_M * CM_PER_M
DETECTOR_SIZE_CM = (DETECTOR_SIZE_X_CM, DETECTOR_SIZE_Y_CM, DETECTOR_SIZE_Z_CM)

DETECTOR_SIZE_X_MM = DETECTOR_SIZE_X_CM * MM_PER_CM
DETECTOR_SIZE_Y_MM = DETECTOR_SIZE_Y_CM * MM_PER_CM
DETECTOR_SIZE_Z_MM = DETECTOR_SIZE_Z_CM * MM_PER_CM
DETECTOR_SIZE_MM = (DETECTOR_SIZE_X_MM, DETECTOR_SIZE_Y_MM, DETECTOR_SIZE_Z_MM)

# Speed of light in vacuum
C_M = 299792458
C_CM = C_M * CM_PER_M

# Index of refraction of xenon
N_XENON = 1.84

C_XENON_M_PER_S = C_M / N_XENON
C_XENON_CM_PER_S = C_XENON_M_PER_S * CM_PER_M
C_XENON_MM_PER_S = C_XENON_CM_PER_S * MM_PER_CM
C_XENON_MM_PER_NS = C_XENON_MM_PER_S / NS_PER_S