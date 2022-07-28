$(document).ready(function () {
    // login form
    $('.login.ui.form')
        .form({
            fields: {
                email: {
                    identifier: 'email',
                    rules: [{
                        type: 'empty',
                        prompt: '请输入您的电子邮箱'
                    },
                        {
                            type: 'email',
                            prompt: '请输入有效电子邮件'
                        }
                    ]
                },
                password: {
                    identifier: 'password',
                    rules: [{
                        type: 'empty',
                        prompt: '请输入您的密码'
                    },
                        {
                            type: 'minLength[6]',
                            prompt: '您的密码必须至少为 6 个字符'
                        }
                    ]
                }
            }
        });

    // register form
    $('.register.ui.form')
        .form({
            inline: true,
            fields: {
                nickname: {
                    identifier: 'nickname',
                    rules: [{
                        type: 'empty',
                        prompt: '请输入你的名字'
                    },
                        {
                            type: 'maxLength[12]',
                            prompt: '您的昵称不得超过 {ruleValue} 个字符'
                        }
                    ]
                },
                email: {
                    identifier: 'email',
                    rules: [{
                        type: 'empty',
                        prompt: '请输入您的电子邮箱'
                    },
                        {
                            type: 'email',
                            prompt: '请输入有效电子邮件'
                        }
                    ]
                },
                password: {
                    identifier: 'password',
                    rules: [{
                        type: 'empty',
                        prompt: '请输入密码'
                    },
                        {
                            type: 'minLength[6]',
                            prompt: '您的昵称不得超过 {ruleValue} 个字符'
                        }
                    ]
                },
                password2: {
                    identifier: 'password2',
                    rules: [{
                        type: 'empty',
                        prompt: '请输入密码'
                    },
                        {
                            type: 'minLength[6]',
                            prompt: '您的昵称不得超过 {ruleValue} 个字符'
                        },
                        {
                            type: 'match[password]',
                            prompt: '您的确认密码必须与密码字段的值匹配'
                        }
                    ]
                },

                terms: {
                    identifier: 'terms',
                    rules: [{
                        type: 'checked',
                        prompt: '您必须同意条款和条件/doge'
                    }]
                }
            }
        });

    // profile form
    $('.profile.ui.form')
        .form({
            inline: true,
            fields: {
                nickname: {
                    identifier: 'nickname',
                    rules: [{
                        type: 'empty',
                        prompt: '请输入你的名字'
                    },
                        {
                            type: 'maxLength[12]',
                            prompt: '您的昵称不得超过 {ruleValue} 个字符'
                        }
                    ]
                },
                github: {
                    identifier: 'github',
                    optional: true,
                    rules: [{
                        type: 'url',
                        prompt: '请输入有效网址'
                    }]
                },
                website: {
                    identifier: 'website',
                    optional: true,
                    rules: [{
                        type: 'url',
                        prompt: '请输入有效网址'
                    }]
                },

                bio: {
                    identifier: 'bio',
                    optional: true,
                    rules: [{
                        type: 'maxLength[25]',
                        prompt: '您的简绍不得超过 {ruleValue} 个字符'
                    }]
                }
            }
        });
});
