
-- shorter alias for function
local directory = pandoc.path.directory

local METADATA = {}

function dump(o)
   if type(o) == 'table' then
      local s = '{ '
      for k,v in pairs(o) do
         if type(k) ~= 'number' then k = '"'..k..'"' end
         s = s .. '['..k..'] = ' .. dump(v) .. ','
      end
      return s .. '} '
   else
      return tostring(o)
   end
end

local DOCDIR = pandoc.system.get_working_directory() .. "/docs/"

function image (img)
  if not img.src:find 'http' then
    local path = directory(directory(METADATA["path"]))
    local relroot = pandoc.path.make_relative("/",path,true)
      img.src = relroot .. img.src
    io.stderr:write(img.src .. "\n")
    return img
  end
end


return {
  -- First get document metadata and store
  -- globally
  {Meta = function (m) METADATA=m end},
  -- Then apply filters
  {Image = image}
}

