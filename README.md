# Ansible Collection - the_new_flesh.dev_roles

A collectiom of 50 Ansible for setting up a Ubuntu 16.04 or 20.04 machine for
computer vision and visual effects development workflows.

# Roles
| Name                             | Type    | Description                                                              | Package Type |
| -------------------------------- | ------- | ------------------------------------------------------------------------ | ------------ |
| autostart                        | config  | configures startup scripts                                               |              |
| aws_cli                          | install | installs awscli                                                          | snap         |
| aws_config                       | config  | configures aws                                                           |              |
| blender                          | install | installs blender                                                         | snap         |
| blender_config                   | config  | configures blender                                                       |              |
| compiz_config                    | config  | configures compizconfig-settings-manager                                 |              |
| compizconfig_settings_manager    | install | installs compizconfig-settings-manager                                   | apt          |
| conda_config                     | config  | configures conda                                                         |              |
| conky                            | install | installs conky                                                           |              |
| conky_config                     | config  | configures conky                                                         |              |
| cufflinks_config                 | config  | configures cufflinks                                                     |              |
| dcc_plugin                       | install | installation of custom plugins for digital content creation applications |              |
| dconf_config                     | config  | configures dconf                                                         |              |
| foundry_licensing_utility        | install | installs foundry-licensing-utility                                       | deb          |
| foundry_licensing_utility_config | config  | configures foundry                                                       |              |
| gnome_tweak_tool                 | install | install gnome-tweak-tool                                                 | apt          |
| gsettings_config                 | config  | configures gsettings                                                     |              |
| handbrake                        | install | installs handbrake                                                       | snap         |
| hardinfo                         | install | installs hardinfo                                                        | apt          |
| houdini_config                   | config  | configures houdini                                                       |              |
| jupyter_config                   | config  | configures jupyter                                                       |              |
| jupyter_nbextensions             | install | install jupyter notebook extensions                                      |              |
| jupyterhub_config                | config  | configures jupyterhub                                                    |              |
| konsole                          | install | installs konsole                                                         | apt          |
| konsole_config                   | config  | configures konsole                                                       |              |
| ksysguard                        | install | installs ksysguard                                                       | apt          |
| linux_hotkeys                    | config  | configures gnome and kbd hotkeys                                         |              |
| meld                             | install | installs meld                                                            | apt          |
| modo_config                      | config  | configures modo                                                          |              |
| nautilus_actions                 | install | installs nautilus-action-configuration-tool                              | apt          |
| nautilus_actions_config          | config  | configures nautilus actions                                              |              |
| nuke_config                      | config  | configures nuke                                                          |              |
| nvidia                           | install | installs nvidia drivers                                                  | apt          |
| nvidia_utils                     | install | installs nvidia-utils                                                    | apt          |
| ohmyzsh                          | install | installs oh-my-zsh                                                       |              |
| parallel                         | install | installs gnu-parallel                                                    | apt          |
| redshift_gtk                     | install | installs redshift-gtk                                                    | apt          |
| shell_config                     | config  | configures shell                                                         |              |
| slack                            | config  | configures shell environment files (.bashrc, .zshrc)                     | snap         |
| stacer                           | install | installs stacer                                                          | apt          |
| sublime                          | install | installs subblime text editor                                            | apt          |
| sublime_config                   | config  | configures sublime text editor                                           |              |
| tree                             | install | installs tree                                                            | apt          |
| unity_tweak_tool                 | install | installs unity-tweak-tool                                                | apt          |
| visual_studio_code               | install | installs visual studio code                                              | snap         |
| visual_studio_code_config        | config  | configures visual studio code and installs extensions                    |              |
| vlc                              | install | installs vlc video application                                           | snap         |
| xclip                            | install | installs xclip                                                           | apt          |
| xkb_key_bindings                 | config  | configures xkb key bindings                                              |              |
| xsel                             | install | installs xsel                                                            | apt          |
