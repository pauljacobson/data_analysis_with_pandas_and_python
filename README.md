# Data Analysis with Python and Pandas

This is an illustrative repo containing dummy data that I'm using to troubleshoot my scripts

## My goals

I have data in Markdown files, one for each work day. These are basically work journals that I use to document my work.

You can see what the data looks like in the `dummy_data.md` file.

My goal is to use a tool like Pandas to read each file, and extract data into a dataframe or `CSV` file (whichever is faster) in the following format:

| Date        |  Entry  | ticket  | chat    | other_tag | project_sales | narrative |
| ----------- | ------ | ------- | ------- | --------- | --------- | ------- |
| Date string |  String (full entry without the line number) | Boolean | Boolean | Boolean   | Boolean   | String | 

The `Booleans` should just be `True` or `False` where a row contains a regex pattern match corresponding with the `ticket`, `chat`, `other_tag`, and `project_sales` column titles (also entry types).

## Why I am doing this

My broad goal is to extract data from these Markdown files into something like a dataframe or even a CSV file (whichever is more efficient) so I can answer questions like the following:

- Which tickets or chats did I respond to (I work in a support role)
- Were the interactions tickets or chats?
- Did the interactions fall into specific categories that are designated by hashtags that I add inline? Here I think I just really need a `True` or `False` response.
- What are the entries that are not interactions (for example, just notes about something I reviewed on the day)?

The purpose of this is to help me automate a weekly report on my work for the previous week that includes the following information:

- How many chats and tickets I completed?
- How many interactions from each category (such as `#project_sales` or `#other_tag`)?
- Which interactions are `#project_sales` and tickets/chats (so I can calculate the ratio of both)?
- What else did I do in the week that wasn't a direct support interaction?
