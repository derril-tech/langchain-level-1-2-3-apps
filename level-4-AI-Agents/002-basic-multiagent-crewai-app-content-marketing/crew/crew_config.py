# crew/crew_config.py

"""
Wrapper file to load the Crew from its actual definition.
Keeps the original import path intact: from crew.crew_config import crew
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crew_definition import crew  # ✅ import from root-level definition
