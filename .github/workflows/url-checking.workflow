workflow "Hugo Link Check" {
  resolves = "linkcheck"
  on = "push"
}

action "filter-to-pr-open-synced" {
  uses = "actions/bin/filter@master"
  args = "action 'opened|synchronize'"
}

action "linkcheck" {
  uses = "marccampbell/hugo-linkcheck-action@v0.1.3"
  needs = "filter-to-pr-open-synced"
  secrets = ["GITHUB_TOKEN"]
  env = {
    HUGO_ACTION_COMMENT	= "false",
    HUGO_STARTUP_WAIT = 20,
  }
}