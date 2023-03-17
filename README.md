# Data Analysis with Python and Pandas

This is an illustrative repo containing dummy data that I'm using to troubleshoot my scripts

## My goal

I have data in Markdown files, one for each work day. These are basically work journals that I use to document my work.

You can see what the data looks like in the `dummy_data.md` file.

My goal is to use a tool like Pandas to read each file, and extract data into a dataframe or `CSV` file (whichever is faster) in the following format:

| Date        |  Entry  | ticket  | chat    | other_tag | project_sales | narrative |
| ----------- | ------ | ------- | ------- | --------- | --------- | ------- |
| Date string |  String (full entry without the line number) | Boolean | Boolean | Boolean   | Boolean   | String | 

The `Booleans` should just be `True` or `False` where a row contains a regex pattern match corresponding with the `ticket`, `chat`, `other_tag`, and `project_sales` column titles (also entry types).
