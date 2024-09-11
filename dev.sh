. ./wootmux.sh

SESSION_NAME=repeat_code
if [ "$(wm_session_exists $SESSION_NAME)" ]; then
  echo "attaching to existing session"
  wm_session_attach $SESSION_NAME
  exit 0
fi

wm_session_new $SESSION_NAME

wm_use_clipboard

wm_pane_new_left "$(wm_pane_current)" "nvim;zsh"

wm_session_attach $SESSION_NAME
