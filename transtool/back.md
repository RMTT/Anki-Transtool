{% for k,v in means.items() %}
### {{ k }} <br>
{% for i in v %}
+ {{ i }} <br>
{% endfor %}
--- <br>
{% endfor %}
