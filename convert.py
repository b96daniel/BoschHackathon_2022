def convert_real2px(real_pos, m2px):
    """Converts a position from the real world coordinate system to the appropriate GUI position."""
    return real_pos[0] * m2px + 490, - real_pos[1] * m2px + 250
