

consoler = ['''<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>New project</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
        <script src="main.js"></script>
    </head>
    <body>

    '''
    ,
            ''' 
            </body>
            </html>''']

def html_tools(style):

    html_tool = {'searchbar': '''<nav>
                            <div class="nav-wrapper z-depth-4">
                              <form>
                                <div class="input-field z-depth-4">
                                  <input id="search" type="search" required>
                                  <label class="label-icon right" for="search"><i class="material-icons">maps</i></label>
                                  <i class="material-icons">close</i>
                                </div>
                              </form>
                            </div>
                        </nav>''',
                 'button': '<button class="btn btn-large black">Read More</button>',
                 'random_para': '<h4 class="truncate">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sit porro eius esse, qui sequi tempore impedit ea, similique nulla neque ad velit minus deleniti quibusdam laborum voluptatem explicabo! Blanditiis, expedita.</h4>',
                 'list': '''<ul class="collection">
                  <li class="collection-item">Item 1</li>
                  <li class="collection-item">Item 2</li>
                  <li class="collection-item">Item 3</li>
                  <li class="collection-item">Item 4</li>
                </ul>''',
                 'header': '''<h2 style= font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; ''' + style + ''' >Header</h2>''',
                 'input_text_label': '''<div class="input-field" ''' + style + '''>
                   <input type="text" id="label">
                   <label class="active" for="name">here</label>
                 </div>''',
                 'input_text': '''<div class="input-field" ''' + style + '''>
                       <input type="text" id="label">
                     </div>''',
                 'input_textarea_label': '''<div class="input-field" ''' + style + ''' >
                   <textarea type="textarea" id="textarea" class="materialize-textarea"></textarea>
                   <label class="active" for="textarea">Textarea</label>
                 </div>''',
                 'input_textarea': '''<div class="input-field" ''' + style + ''' >
                       <textarea type="textarea" id="textarea" class="materialize-textarea"></textarea>
                     </div>''',
                 'label': '''<label class="active" for="name"> label </label>'''
                 ,
                 'grid_div2': '''<div class="row">
               <div class="col s6"><div class="card-panel grey">boop</div></div>
             </div>''',
                 'navig': '''<nav>
                <div class="nav-wrapper blue">
                  <h3 class="center"> heading </h3>
                  </div>
              </nav>'''
                 }

    return html_tool