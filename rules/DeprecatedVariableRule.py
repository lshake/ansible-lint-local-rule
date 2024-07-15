from __future__ import annotations

from ansiblelint.rules import AnsibleLintRule

class DeprecatedVariableRule(AnsibleLintRule):
    """Deprecated variable declarations."""
    id = 'LSHAKE001'
    description = 'Check for lines that have old style variable declarations'
    tags = { 'deprecations' }
    severity = "HIGH"
    version_added = "6.14.3"

    def match(self, line: str) -> Union[bool, str]:
        if '##' in line:
            return 'old style variable names'
        else:
            return False
